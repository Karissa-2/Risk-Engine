import numpy as np
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


def ece(y_true, confidence, bins=10):
    y_true = np.asarray(y_true, dtype=float)
    confidence = np.asarray(confidence, dtype=float)
    if y_true.ndim != 1 or confidence.ndim != 1 or y_true.shape != confidence.shape:
        raise ValueError("y_true and confidence must be one-dimensional arrays of equal length")
    if y_true.size == 0:
        raise ValueError("y_true and confidence must not be empty")
    if bins < 1:
        raise ValueError("bins must be at least 1")
    if np.any((confidence < 0) | (confidence > 1)):
        raise ValueError("confidence values must be between 0 and 1")

    bin_ids = np.minimum((confidence * bins).astype(int), bins - 1)
    error = 0.0
    for index in range(bins):
        in_bin = bin_ids == index
        if np.any(in_bin):
            error += in_bin.mean() * abs(y_true[in_bin].mean() - confidence[in_bin].mean())
    return float(error)


def multiclass_brier(y_idx, P):
    P = np.asarray(P)
    onehot = np.eye(P.shape[1])[np.asarray(y_idx)]
    return float(((P - onehot) ** 2).sum(axis=1).mean())


def top_label_ece(y_idx, P, bins=10):
    y_idx, P = np.asarray(y_idx), np.asarray(P)
    conf = P.max(axis=1)
    right = (P.argmax(axis=1) == y_idx).astype(float)
    return ece(right, conf, bins)


def report_multiclass(name, y_idx, P, bins=10):
    P = np.asarray(P)
    n_classes = P.shape[1]
    Pc = np.clip(P, 1e-6, 1)
    Pc = Pc / Pc.sum(axis=1, keepdims=True)
    metrics = {
        "accuracy": float((P.argmax(axis=1) == np.asarray(y_idx)).mean()),
        "brier": multiclass_brier(y_idx, P),
        "log_loss": float(log_loss(y_idx, Pc, labels=list(range(n_classes)))),
        "top_label_ece": top_label_ece(y_idx, P, bins),
    }
    print(f"{name:<24} acc {metrics['accuracy']:.4f}  Brier {metrics['brier']:.4f}  "
          f"logloss {metrics['log_loss']:.4f}  "
          f"top-label ECE {metrics['top_label_ece']:.4f}")
    return metrics


def evaluate_multiclass_model(name, model, X, y_true, bins=10):
    """Evaluate a fitted classifier that exposes predict_proba and classes_."""
    if not hasattr(model, "predict_proba") or not hasattr(model, "classes_"):
        raise ValueError("model must be fitted and expose predict_proba() and classes_")

    probabilities = np.asarray(model.predict_proba(X))
    classes = np.asarray(model.classes_)
    if probabilities.ndim != 2 or probabilities.shape[1] != classes.size:
        raise ValueError("predict_proba output columns must match model.classes_")

    class_indices = {label: index for index, label in enumerate(classes)}
    try:
        y_idx = np.asarray([class_indices[label] for label in np.asarray(y_true)])
    except KeyError as error:
        raise ValueError("y_true contains a class not seen during model training") from error

    return report_multiclass(name, y_idx, probabilities, bins)


def reliability_grid(panels, title=""):
    n = len(panels)
    cols = 2
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4.5 * rows), squeeze=False)
    for ax, (tname, curves) in zip(axes.ravel(), panels.items()):
        ax.plot([0, 1], [0, 1], "k--", label="perfect")
        for label, (y, p) in curves.items():
            if np.asarray(y).sum() < 20:
                continue   # too few attacks for a meaningful curve
            frac_pos, mean_pred = calibration_curve(y, p, n_bins=10)
            ax.plot(mean_pred, frac_pos, marker="o", label=label)
        ax.set_title(tname)
        ax.set_xlabel("Predicted probability")
        ax.set_ylabel("Observed frequency")
        ax.legend(fontsize=8)
    fig.suptitle(title)
    fig.tight_layout()
    plt.show()