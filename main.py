import sys
import os
import csv
import readability
import text_metrics

FOLDER = "./data"

def get_category(filename):
    """Extracts category name from filename like 'youth_cookienotice.txt' -> 'youth'"""
    base = os.path.basename(filename)
    category = base.split("_")[0]
    return category

def process_file(filepath):
    """Reads, cleans, and computes all metrics for one file. Returns a dict (one row)."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        raw_text = f.read()

    cleaned = text_metrics.cleaning_file(raw_text)

    row = {
        "category": get_category(filepath),
        "flesch_ease": readability.get_flesch_reading(cleaned),
        "fk_grade": readability.get_flesch_kincaid(cleaned),
        "smog": readability.get_smog(cleaned),
        "gunning_fog": readability.get_gunning(cleaned),
        "dale_chall": readability.get_dale(cleaned),
        "difficult_words_ratio": readability.get_difficult(cleaned, cleaned.split()),
        "avg_sentence_length": text_metrics.sentence_length(cleaned),
        "vague_word_ratio": text_metrics.vague_find(cleaned),
    }
    return row

def main():
    files = [
        os.path.join(FOLDER, "youth_cookienotice.txt"),
        os.path.join(FOLDER, "middleAged_cookienotice.txt"),
        os.path.join(FOLDER, "senior_cookienotice.txt"),
    ]

    rows = [process_file(f) for f in files]

    output_path = "./results/results.csv"
    os.makedirs("./results", exist_ok=True)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved results to {output_path}")

if __name__ == "__main__":
    main()
