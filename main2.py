import sys
import os
import csv
import readability
import text_metrics

FOLDER = "./data"

def get_category(filepath):
    """Extracts category name from filename like 'youth_cookienotice.txt' -> 'youth'"""
    return os.path.basename(os.path.dirname(filepath))

def process_file(filepath):
    """Reads, cleans, and computes all metrics for one file. Returns a dict (one row)."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        raw_text = f.read()

    cleaned = text_metrics.cleaning_file(raw_text)

    words = cleaned.split()

    row = {
        "category": get_category(filepath),
        "filename" : os.path.basename(filepath),
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

def collect_files(base_folder):
    files = []
    for root, _, filenames in os.walk(base_folder):
        for name in filenames:
            if name.endswith(".txt"):
                files.append(os.path.join(root, name))
    return files


def main():
    files = collect_files(FOLDER)
    rows = [process_file(f) for f in files]

    output_path = "./results/results2.csv"
    os.makedirs("./results", exist_ok=True)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved results to {output_path}")


if __name__ == "__main__":
    main()
