import argparse

from tabulate import tabulate

from .readers import FileReader
from .settings import get_report


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)

    args = parser.parse_args()

    rows = FileReader.read_csv_files(args.files)

    report = get_report(args.report)
    report_data = report.generate(rows)

    print(tabulate(report_data, headers="keys", tablefmt="grid"))
