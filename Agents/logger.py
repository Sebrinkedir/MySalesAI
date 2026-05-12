import csv
import os
from datetime import datetime


class Logger:

    def log_run(self, mode, question, analysis, insights, latency=None):

        log_file = "logs/evaluation_log.csv"

        file_exists = os.path.isfile(log_file)

        with open(log_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "timestamp",
                    "mode",
                    "question",
                    "analysis",
                    "insights",
                    "latency_seconds"
                ])

            writer.writerow([
                datetime.now(),
                mode,
                question,
                analysis,
                insights,
                latency
            ])