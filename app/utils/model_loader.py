import joblib
import os

MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'models'))


def load_classifier():
    return joblib.load(os.path.join(MODELS_DIR, "emi_eligibility_classifier.pkl"))


def load_regressor():
    return joblib.load(os.path.join(MODELS_DIR, "max_emi_regressor.pkl"))


def load_label_encoder():
    return joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))


def load_scaler():
    return joblib.load(os.path.join(MODELS_DIR, "feature_scaler.pkl"))