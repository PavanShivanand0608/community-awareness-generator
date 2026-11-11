
import joblib
import json
from pathlib import Path

MODEL_PATH = Path("notebooks/models/linear_svm_baseline.joblib")
CONFIG_PATH = Path("notebooks/models/baseline_config.json")

model = joblib.load(MODEL_PATH)

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

label_ids = config["label_ids"]


def predict_sdgs(text):
    # Validate input type
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Remove unnecessary spaces
    text = text.strip()

    # Validate empty input
    if not text:
        raise ValueError("Input cannot be empty.")

    # Validate minimum length
    if len(text) < 20:
        raise ValueError("Input must contain at least 20 characters.")

    # Generate prediction
    prediction = model.predict([text])

    predicted_indices = prediction[0].nonzero()[0]

    predicted_label_ids = [
        label_ids[index] for index in predicted_indices
    ]

    return predicted_label_ids
