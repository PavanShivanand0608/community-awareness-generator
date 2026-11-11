
import pytest
from src.predictor import predict_sdgs


def test_valid_education_text():
    result = predict_sdgs(
        "Improving access to quality education for children."
    )
    assert isinstance(result, list)
    assert all(isinstance(label, int) for label in result)


def test_empty_text():
    with pytest.raises(ValueError):
        predict_sdgs("")


def test_whitespace_text():
    with pytest.raises(ValueError):
        predict_sdgs("   ")


def test_short_text():
    with pytest.raises(ValueError):
        predict_sdgs("Education")


def test_non_string_input():
    with pytest.raises(ValueError):
        predict_sdgs(123)
