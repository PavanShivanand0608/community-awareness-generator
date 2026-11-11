
import joblib
import json
from pathlib import Path

MODEL_PATH = Path("notebooks/models/linear_svm_baseline.joblib")
CONFIG_PATH = Path("notebooks/models/baseline_config.json")

print("Loading trained model...")
model = joblib.load(MODEL_PATH)

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

label_ids = config["label_ids"]

print("Model loaded successfully!")

test_texts = [
    "Improving access to quality education for children.",
    "Promoting clean energy and affordable electricity.",
    "Providing clean drinking water and sanitation facilities."
]

predictions = model.predict(test_texts)

for i, text in enumerate(test_texts):
    predicted_indices = predictions[i].nonzero()[0]
    predicted_label_ids = [label_ids[index] for index in predicted_indices]

    print("\nText:", text)
    print("Predicted SDG IDs:", predicted_label_ids)
