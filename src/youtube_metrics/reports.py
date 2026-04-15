from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: list[dict]) -> list[dict]:
        pass


class ClickbaitReport(BaseReport):
    def generate(self, videos: list[dict]) -> list[dict]:
        clickbaits = []

        for video in videos:
            if video["ctr"] > 15 and video["retention_rate"] < 40:
                clickbait_video = {
                    "title": video["title"],
                    "ctr": video["ctr"],
                    "retention_rate": video["retention_rate"],
                }

                clickbaits.append(clickbait_video)

        clickbaits.sort(key=lambda x: x["ctr"], reverse=True)

        return clickbaits
