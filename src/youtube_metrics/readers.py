import csv


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
