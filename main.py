import argparse
import csv

from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)

    args = parser.parse_args()

    rows = []
    for file_path in args.files:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row["title"]
                ctr = float(row["ctr"])
                retention_rate = float(row["retention_rate"])

                if ctr > 15 and retention_rate < 40:
                    rows.append(
                        {
                            "title": title,
                            "ctr": ctr,
                            "retention_rate": retention_rate,
                        }
                    )
                    
    rows.sort(key=lambda x: x["ctr"], reverse=True)

    print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
