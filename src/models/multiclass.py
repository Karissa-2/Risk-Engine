# src/models/multiclass.py
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from src.data.preprocess import prep

def build_multiclass_pipeline():
    return Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=3000))])