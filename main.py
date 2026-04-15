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

        filtered_rows.sort(key=lambda x: x["ctr"], reverse=True)

        return filtered_rows


class FileReader:
    @staticmethod
    def read_csv_files(files):
        rows = []

        for file_path in files:
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

        return rows


REPORTS = {
    "clickbait": ClickbaitReport,
}


def get_report(report_name):
    try:
        ReportType = REPORTS[report_name]
        return ReportType()
    except KeyError:
        raise ValueError(f"Неизвестый тип репорта: {report_name}")
        


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)

    args = parser.parse_args()

    rows = FileReader.read_csv_files(args.files)

    report = get_report(args.report)
    report_data = report.generate(rows)

    print(tabulate(report_data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
