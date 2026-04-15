import csv


class FileReader:
    @staticmethod
    def read_csv_files(files: list[str]) -> list[dict]:
        videos = []

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    video = {
                        "title": row["title"],
                        "ctr": float(row["ctr"]),
                        "retention_rate": int(row["retention_rate"]),
                        "views": int(row["views"]),
                        "likes": int(row["likes"]),
                        "avg_watch_time": float(row["avg_watch_time"]),
                    }
                    videos.append(video)

        return videos
