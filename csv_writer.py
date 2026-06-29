from pathlib import Path
import csv


class CsvWriter:
    def __init__(self, filename: str):
        self.filename = Path(filename)
        self.columns = ["uuid", "name", "specialization", "city", "phone"]

        self.filename.parent.mkdir(parents=True, exist_ok=True)

        if not self.filename.exists() or self.filename.stat().st_size == 0:
            with self.filename.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.columns)
                writer.writeheader()

    def write_rows(self, rows: list[dict]):
        with self.filename.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=self.columns,
                extrasaction="ignore",
            )
            writer.writerows(rows)
