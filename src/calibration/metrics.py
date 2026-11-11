from xml.parsers.expat import model
import numpy as np
from sklearn.metrics import log_loss, brier_score_loss
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

# Expected Calibration Error (ECE): Shows how far the probability given by the model is from the real result. 0 = Model is perfectly calibrated. 
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

# Multiclass Brier score: Gives the average squared difference between the predicted probabilities and the real answer. (Once again, 0 = perfect calibration)
def multiclass_brier(y_idx, P):
    P = np.asarray(P)
    onehot = np.eye(P.shape[1])[np.asarray(y_idx)]
    return float(((P - onehot) ** 2).sum(axis=1).mean())

# Top-Label ECE: Calibration of the model's confidence in the specific class it predicted.
def top_label_ece(y_idx, P, bins=10):
    y_idx, P = np.asarray(y_idx), np.asarray(P)
    conf = P.max(axis=1)
    right = (P.argmax(axis=1) == y_idx).astype(float)
    return ece(right, conf, bins)

#Returns calibration metrics for a model with multiple classes.
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

#Assists multiclass function with returning metrics for a binary model.
def report_binary(name, y_true, p_pos, bins=10):
    """Calibration metrics for a binary model; p_pos = probability of class 1."""
    y_true = np.asarray(y_true).astype(int)
    p_pos = np.asarray(p_pos, dtype=float)
    pc = np.clip(p_pos, 1e-6, 1 - 1e-6)
    metrics = {
        "accuracy": float(((p_pos > 0.5).astype(int) == y_true).mean()),
        "brier": float(brier_score_loss(y_true, p_pos)),
        "log_loss": float(log_loss(y_true, pc, labels=[0, 1])),
        "ece": ece(y_true, p_pos, bins),
    }
    print(f"{name:<24} acc {metrics['accuracy']:.4f}  Brier {metrics['brier']:.4f}  "
          f"logloss {metrics['log_loss']:.4f}  ECE {metrics['ece']:.4f}")
    return metrics

#Runs report_multiclass or report_binary (depending on the number of classes in the model) directly. Also produces a reliability diagram if plot=True.
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

#Creates the reliability diagrams/calibration curves for the model. Two per row, one for each class. The closer the curve is to the diagonal line, the better calibrated the model is.
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

#Combines all the functions above to create one full report for the model.
#Call this function in the jupyter notebook to get the calibration report for the model.
    def calibration_report(name, model, X, y_true, bins=10, plot=True):
        """Run all calibration metrics (and optionally the reliability plot) for a fitted model."""
        if not hasattr(model, "predict_proba") or not hasattr(model, "classes_"):
            raise ValueError("model must be fitted and expose predict_proba() and classes_")

        probabilities = np.asarray(model.predict_proba(X))
        classes = list(model.classes_)

        if len(classes) == 2:
            p_pos = probabilities[:, 1]
            y_bin = (np.asarray(y_true) == classes[1]).astype(int)
            metrics = report_binary(name, y_bin, p_pos, bins)
            if plot:
                reliability_grid({name: {"model": (y_bin, p_pos)}},
                                title=f"Reliability Diagram: {name}")
        else:
            metrics = evaluate_multiclass_model(name, model, X, y_true, bins)

        return metrics