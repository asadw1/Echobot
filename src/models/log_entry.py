from dataclasses import dataclass
from datetime import datetime
from textwrap import fill

@dataclass
class LogEntry:
    timestamp: datetime
    summary: str
    echobotSummaryId: int = 0  # assigned by LogRepository on save

    def to_dict(self):
        """
        Convert the log entry into a dictionary format with line breaks for long summaries.
        """
        formatted_summary = fill(self.summary, width=140)  # Break lines at 140 characters
        return {
            "echobotSummaryId": self.echobotSummaryId,
            "timestamp": self.timestamp.isoformat(),
            "summary": formatted_summary
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Create a LogEntry instance from a dictionary.
        """
        return LogEntry(
            echobotSummaryId=data.get("echobotSummaryId", 0),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            summary=data["summary"]
        )
