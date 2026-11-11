
from src.predictor import predict_sdgs

test_texts = [
    "",
    "   ",
    "Education",
    "The",
    "Improving access to quality education for children."
]

for text in test_texts:
    print("\nInput:", repr(text))

    try:
        result = predict_sdgs(text)
        print("Predicted SDG IDs:", result)

    except ValueError as error:
        print("Validation error:", error)
