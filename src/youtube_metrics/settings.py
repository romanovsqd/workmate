from .reports import ClickbaitReport

REPORTS = {
    "clickbait": ClickbaitReport,
}


def get_report(report_name):
    try:
        ReportType = REPORTS[report_name]
        return ReportType()
    except KeyError:
        raise ValueError(f"Неизвестый тип отчета: {report_name}")
