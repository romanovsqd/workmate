import pytest

from youtube_metrics.reports import ClickbaitReport
from youtube_metrics.settings import get_report


@pytest.fixture
def videos():
    return [
        {
            "title": "A",
            "ctr": 18.0,
            "retention_rate": 35,
            "views": 1200,
            "likes": 150,
            "avg_watch_time": 45.5,
        },
        {
            "title": "B",
            "ctr": 22.0,
            "retention_rate": 30,
            "views": 980,
            "likes": 120,
            "avg_watch_time": 38.2,
        },
        {
            "title": "C",
            "ctr": 10.0,
            "retention_rate": 20,
            "views": 500,
            "likes": 40,
            "avg_watch_time": 22.7,
        },
        {
            "title": "D",
            "ctr": 25.0,
            "retention_rate": 50,
            "views": 2000,
            "likes": 310,
            "avg_watch_time": 60.3,
        },
    ]


@pytest.fixture
def clickbait_report():
    return ClickbaitReport()


def test_get_report_returns_clickbait_report():
    report = get_report("clickbait")

    assert isinstance(report, ClickbaitReport)


def test_get_report_raises_unknown_error():
    with pytest.raises(ValueError) as e:
        get_report("does_not_exist")

    assert "Unknown report type" in str(e.value)


def test_clickbait_filter(clickbait_report, videos):
    result = clickbait_report.generate(videos)

    titles = [v["title"] for v in result]

    assert titles == ["B", "A"]
    assert all(v["ctr"] > 15 for v in result)
    assert all(v["retention_rate"] < 40 for v in result)


def test_clickbait_report_output_format(clickbait_report, videos):
    expected_keys = {"title", "ctr", "retention_rate"}

    result = clickbait_report.generate(videos)

    for video in result:
        assert set(video.keys()) == expected_keys
