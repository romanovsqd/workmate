import argparse
import csv
from abc import ABC, abstractmethod

from tabulate import tabulate


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data):
        pass


class ClickbaitReport(BaseReport):
    def generate(self, rows):
        filtered_rows = []

        for row in rows:
            if row["ctr"] > 15 and row["retention_rate"] < 40:
                filtered_rows.append(row)

        return filtered_rows


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
                rows.append(
                    {
                        "title": row["title"],
                        "ctr": float(row["ctr"]),
                        "retention_rate": float(row["retention_rate"]),
                    }
                )

    clickbait_report = ClickbaitReport()
    report = clickbait_report.generate(rows)

    report.sort(key=lambda x: x["ctr"], reverse=True)

    print(tabulate(report, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
