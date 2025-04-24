from src.models.log_entry import LogEntry
from src.storage.log_repository import LogRepository
from datetime import datetime

class Summarizer:
    def __init__(self, repository: LogRepository):
        """
        Initialize the Summarizer with a LogRepository instance.
        """
        self.repository = repository

    def create_summary(self, summary_text: str):
        """
        Create a summary and save it to the repository.
        :param summary_text: Text summarizing the conversation.
        """
        entry = LogEntry(timestamp=datetime.now(), summary=summary_text)
        self.repository.save_log(entry)

    def retrieve_summaries(self, limit: int = 5):
        """
        Retrieve the most recent summaries.
        :param limit: Maximum number of summaries to retrieve.
        :return: List of LogEntry instances.
        """
        all_logs = self.repository.get_all_logs()
        return all_logs[-limit:]  # Get the last 'limit' entries
