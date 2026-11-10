#So even though isotonic regression and platt scaling both do the calibrating part, and platt is more logistic regression focused,
#Isotonic is more flexible and can handle non-linear relationships better.
#Both version are included to see which produces better scores, whichever one is better can be used for the final model.
from sklearn.isotonic import IsotonicRegression

def fit_isotonic(raw_cal, y_cal):
    return IsotonicRegression(out_of_bounds="clip").fit(raw_cal, y_cal)