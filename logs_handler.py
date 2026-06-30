from pathlib import Path
from datetime import datetime


class LogsHandler:
    def __init__(self, filename: str):
        self.filename = Path(filename)

        self.filename.parent.mkdir(parents=True, exist_ok=True)

        if not self.filename.exists():
            with self.filename.open("w", newline="", encoding="utf-8") as f:
                f.write(f"{self.filename} logs\n")

    def log_message(self, message: str, type: str):
        if type == "success":
            log_message = f"[Success] {message}"
            print(f"\033[92m{log_message}\033[0m")
        elif type == "fail":
            log_message = f"[Fail] {message}"
            print(f"\033[91m{log_message}\033[0m")
        else:
            log_message = f"[Info] {message}"
            print(f"\033[94m{log_message}\033[0m")


        with self.filename.open("a", newline="", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {log_message}\n")
