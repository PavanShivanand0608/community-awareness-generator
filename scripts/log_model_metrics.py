
import json
import wandb
from pathlib import Path

CONFIG_PATH = Path("notebooks/models/baseline_config.json")

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

run = wandb.init(
    entity="phoenixrising27623-pavan",
    project="community-awareness-sdg-classifier",
    job_type="model-evaluation",
    name="linear-svm-test-metrics"
)

run.log({
    "validation_macro_f1": config["validation_macro_f1"],
    "test_macro_f1": config["test_macro_f1"],
    "test_micro_f1": config["test_micro_f1"],
    "test_micro_precision": config["test_micro_precision"],
    "test_micro_recall": config["test_micro_recall"]
})

run.finish()

print("Model evaluation metrics logged successfully!")
