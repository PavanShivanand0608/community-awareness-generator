#!/usr/bin/env python3
"""Convert the project's existing train/test JSONL into a CSV catalogue for Dolt.
Source JSONL files are read-only; embeddings are intentionally not duplicated.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

FIELDS = ["record_id", "split", "source_file", "source_line", "text",
          "labels_json", "label_count", "language", "text_length",
          "metadata_json", "text_sha256"]

def compact_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)

def convert(source, split, writer):
    if not source.is_file():
        raise FileNotFoundError(
            f"Missing {source}. Restore it using your existing DVC workflow first."
        )
    count = 0
    with source.open(encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {source}, line {line_number}: {exc}") from exc
            text = record.get("text", "")
            if not isinstance(text, str):
                text = str(text)
            labels = record.get("labels")
            if labels is None:
                labels = []
            elif not isinstance(labels, list):
                labels = [labels]
            metadata = record.get("metadata", {})
            language = metadata.get("language", "unknown") if isinstance(metadata, dict) else "unknown"
            text_length = record.get("text_length")
            if text_length is None:
                text_length = len(text.split())
            writer.writerow({
                "record_id": f"{split}:{line_number}",
                "split": split,
                "source_file": source.as_posix(),
                "source_line": line_number,
                "text": text,
                "labels_json": compact_json(labels),
                "label_count": len(labels),
                "language": str(language or "unknown"),
                "text_length": int(text_length),
                "metadata_json": compact_json(metadata),
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            })
            count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument("--output", type=Path,
        default=Path("data/processed/dolt_import/sdg_records.csv"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        train_count = convert(root / "data/raw/train.jsonl", "train", writer)
        test_count = convert(root / "data/raw/test.jsonl", "test", writer)
    print(f"Prepared {train_count + test_count:,} records ({train_count:,} train, {test_count:,} test)")
    print(f"CSV: {output}")
    print("Original JSONL files were not modified; embeddings were omitted intentionally.")

if __name__ == "__main__":
    main()
