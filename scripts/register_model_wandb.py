
import wandb
from pathlib import Path

# W&B project details
ENTITY = "phoenixrising27623-pavan"
PROJECT = "community-awareness-sdg-classifier"

# Model files
MODEL_PATH = Path("notebooks/models/linear_svm_baseline.joblib")
CONFIG_PATH = Path("notebooks/models/baseline_config.json")

# Check files
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"Config not found: {CONFIG_PATH}")

# Start W&B run
run = wandb.init(
    entity=ENTITY,
    project=PROJECT,
    job_type="model-registration",
    name="linear-svm-baseline-registration"
)

# Create model artifact
artifact = wandb.Artifact(
    name="community-awareness-sdg-classifier",
    type="model",
    description="Trained TF-IDF and One-vs-Rest Linear SVM baseline model"
)

# Add model and configuration files
artifact.add_file(str(MODEL_PATH))
artifact.add_file(str(CONFIG_PATH))

# Upload artifact to W&B
run.log_artifact(artifact)

# Finish run
run.finish()

print("Model artifact registration submitted successfully!")
