# AI-Assisted Community Awareness Campaign Generator

## Project Overview

This project explores an ML-assisted approach to classifying sustainable development topics in text as an initial component of a community awareness campaign generator. The Phase 1 baseline classifies documents into one or more Sustainable Development Goal (SDG) categories.

**Current scope:** SDG multi-label text classification. Campaign message generation and user-facing campaign workflows are future development tasks.

## Dataset

- **Name:** UNDP SDGi Corpus
- **Source:** https://huggingface.co/datasets/UNDP/sdgi-corpus
- **License:** CC BY-NC-SA 4.0
- **Languages:** English, Spanish, and French
- **Training split:** 5,880 examples
- **Test split:** 1,470 examples
- **Labels:** 17 SDG categories

The project exports the text, labels, and metadata into JSONL files under `data/raw/`. The original embedding field is omitted from these exports because the baseline uses TF-IDF features.

Review the dataset license and obtain any required project-supervisor approval before redistributing the dataset or publishing derived materials.

## Technology Stack

- Python
- Hugging Face Datasets
- pandas and NumPy
- scikit-learn
- TF-IDF text features
- One-vs-Rest classification
- MLflow experiment tracking
- Git and DVC

## Project Structure

```text
community-awareness-generator/
├── data/
│   └── raw/                   # DVC-managed JSONL dataset
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_models.ipynb
│   ├── baseline_evaluation_results.csv
│   └── models/
│       └── baseline_config.json
├── src/
│   └── download_data.py
├── .dvc/
├── .dvcignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If the dataset has already been exported, the notebooks can use the local JSONL files. Otherwise, download the dataset from Hugging Face and follow the export steps in the notebooks.

## Baseline Methodology

The baseline compares three approaches:

1. Dummy classifier as a reference baseline
2. Logistic Regression with TF-IDF features
3. Linear Support Vector Machine (Linear SVM) with TF-IDF features

The classifier uses a One-vs-Rest strategy for multi-label prediction. The training split is divided into training and validation subsets using an 80/20 split with random state 42. The official test split is reserved for final evaluation.

## Initial Results

The selected validation model was Linear SVM.

| Metric | Initial result |
|---|---:|
| Validation macro-F1 | 0.8200 |
| Test macro-F1 | Approximately 0.72 |
| Test micro-F1 | Approximately 0.72 |
| Test micro-precision | Approximately 0.73 |
| Test micro-recall | Approximately 0.71 |

The test metrics are rounded summaries of the initial notebook output. Refer to `notebooks/baseline_evaluation_results.csv` for the recorded values.

## Experiment Tracking and Data Versioning

- MLflow experiment: `sdg-text-classification-baselines`
- Baseline run: `linear-svm-tfidf-baseline`
- DVC tracking file: `data/raw.dvc`

The dataset is available locally and can be retrieved with DVC. A shared DVC remote has not yet been configured.

## Limitations and Next Steps

- The current system classifies SDG topics; it does not yet generate campaign content.
- The validation split is a reproducible random split, not a multi-label-stratified split.
- The difference between validation and test performance requires further investigation.
- The dataset's language distribution and formal-report style may limit generalization to short community campaign messages.
- Further work should include error analysis, class-wise evaluation, reproducibility checks, and supervisor review of dataset usage and licensing.
- Future phases can explore campaign content generation, audience adaptation, and evaluation of generated messages.

## Attribution

Dataset: UNDP SDGi Corpus, available through Hugging Face. Review and comply with the dataset's CC BY-NC-SA 4.0 license and attribution requirements before sharing the dataset or adapted materials.
