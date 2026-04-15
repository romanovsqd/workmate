from .reports import BaseReport, ClickbaitReport

REPORTS = {
    "clickbait": ClickbaitReport,
}


def get_report(report_name: str) -> BaseReport:
    try:
        ReportType = REPORTS[report_name]
        return ReportType()
    except KeyError:
        raise ValueError(f"Unknown report type: {report_name}")
