# Model Risk Assessment

## 1. Dataset Limitations
- The model is trained on the UNDP SDGi Corpus.
- The corpus contains formal sustainability-report passages.
- It may not represent everyday community conversations or awareness messages.

## 2. Language Limitations
- The dataset contains English, French, and Spanish.
- The model has not been validated for Indian regional languages.
- Predictions for unsupported languages may be unreliable.

## 3. Model Performance
- Selected model: Linear SVM.
- Test Macro-F1: 0.7154.
- Test Micro-F1: 0.7215.
- Performance may vary across individual SDG labels.

## 4. Prediction Limitations
- The model can return multiple SDG labels.
- Very short or ambiguous text can produce misleading predictions.
- Linear SVM predictions are not calibrated probabilities.
- The system must not present prediction scores as confidence percentages.

## 5. Input Validation
- Empty text is rejected.
- Whitespace-only text is rejected.
- Text shorter than 20 characters is rejected.
- Non-string input is rejected.

## 6. Future Improvements
- Evaluate performance separately for each SDG.
- Test robustness on real community-awareness messages.
- Evaluate additional languages.
- Explore multilingual transformer models.
- Collect a representative community-awareness dataset.

## 7. Per-SDG Performance Analysis

A classification report was generated to evaluate the
Linear SVM model across all 17 SDG labels.

- Highest F1-score: 0.76 (SDG 11 and SDG 16).
- Lowest F1-score: 0.64 (SDG 7).
- SDG 9 achieved an F1-score of 0.68.
- SDG 5 and SDG 12 achieved F1-scores of 0.69.
- Overall Macro-F1: approximately 0.72.
- Overall Micro-F1: approximately 0.72.

The results indicate that model performance varies
across SDG categories. Further investigation and
additional representative training examples may
help improve weaker categories.


## 8. Label Support and Performance Analysis

The relationship between test-set support and per-label
F1-score was examined.

- Pearson correlation: 0.502.
- This indicates a moderate positive relationship.
- SDG 11 had the highest support (238 examples) and an
  F1-score of 0.764.
- SDG 7 had 64 examples and the lowest F1-score (0.636).
- SDG 14 had only 48 examples but achieved an F1-score
  of 0.706.

The results suggest that the number of test examples
may be related to classification performance. However,
support alone does not explain model performance.
Further investigation of label characteristics and
training data is required.
