from dataclasses import dataclass
from datetime import datetime
from textwrap import fill  # Import to handle line-breaking for long strings

@dataclass
class LogEntry:
    timestamp: datetime
    summary: str

    def to_dict(self):
        """
        Convert the log entry into a dictionary format with line breaks for long summaries.
        """
        formatted_summary = fill(self.summary, width=140)  # Break lines at 140 characters
        return {
            "timestamp": self.timestamp.isoformat(),
            "summary": formatted_summary
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Create a LogEntry instance from a dictionary.
        """
        return LogEntry(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            summary=data["summary"]
        )
