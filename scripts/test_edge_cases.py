
import joblib
from pathlib import Path

MODEL_PATH = Path("notebooks/models/linear_svm_baseline.joblib")

model = joblib.load(MODEL_PATH)

test_cases = [
    "",
    "Education",
    "Water",
    "The"
]

for text in test_cases:
    print("\nInput:", repr(text))

    try:
        prediction = model.predict([text])
        predicted_indices = prediction[0].nonzero()[0]

        print("Prediction indices:", predicted_indices.tolist())

    except Exception as error:
        print("Error:", error)
