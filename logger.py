from datetime import datetime

class Logger:
    def log(self, message):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()} - {message}\n")