import argparse
import sys

from tabulate import tabulate

from .readers import FileReader
from .settings import get_report


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)

    args = parser.parse_args()

    try:
        videos = FileReader.read_csv_files(args.files)

        report = get_report(args.report)
        report_data = report.generate(videos)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(tabulate(report_data, headers="keys", tablefmt="grid"))
