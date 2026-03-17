import json
from src.models.log_entry import LogEntry
from src.config import get_data_path

class LogRepository:
    def __init__(self, file_path=None):
        """
        Initialize the repository with a file path for local storage.
        """
        self.file_path = file_path if file_path is not None else get_data_path()

    def _read_store(self) -> dict:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"totalSummaryCount": 0, "entries": []}

    def _write_store(self, store: dict):
        with open(self.file_path, 'w') as f:
            json.dump(store, f, indent=2)

    def save_log(self, entry: LogEntry):
        """
        Assign the next auto-incremented echobotSummaryId, append the entry,
        and update totalSummaryCount — all in a single atomic write.
        :param entry: LogEntry instance to save.
        """
        store = self._read_store()
        new_id = store["totalSummaryCount"] + 1
        entry.echobotSummaryId = new_id
        store["entries"].append(entry.to_dict())
        store["totalSummaryCount"] = new_id
        self._write_store(store)

    def get_all_logs(self) -> list:
        """
        Retrieve all log entries from the file.
        :return: List of LogEntry instances.
        """
        store = self._read_store()
        return [LogEntry.from_dict(e) for e in store["entries"]]
