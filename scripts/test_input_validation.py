
def validate_text(text):
    if not isinstance(text, str):
        return False, "Input must be a string."

    cleaned_text = text.strip()

    if not cleaned_text:
        return False, "Input cannot be empty."

    if len(cleaned_text) < 20:
        return False, "Input must contain at least 20 characters."

    return True, "Input is valid."


test_cases = [
    "",
    "   ",
    "Education",
    "The",
    "Improving access to quality education for children."
]

for text in test_cases:
    is_valid, message = validate_text(text)

    print("\nInput:", repr(text))
    print("Valid:", is_valid)
    print("Message:", message)
