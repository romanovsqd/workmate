from abc import ABC, abstractmethod


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
