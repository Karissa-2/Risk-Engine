import numpy as np
from sklearn.linear_model import LogisticRegression

class PlattCalibrator:
    def fit(self, raw, y):
        self.lr = LogisticRegression().fit(np.asarray(raw).reshape(-1, 1), y)
        return self

    def predict(self, raw):
        return self.lr.predict_proba(np.asarray(raw).reshape(-1, 1))[:, 1]