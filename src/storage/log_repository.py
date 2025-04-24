import json
from src.models.log_entry import LogEntry

class LogRepository:
    def __init__(self, file_path='chat_log.json'):
        """
        Initialize the repository with a file path for local storage.
        """
        self.file_path = file_path

    def save_log(self, entry: LogEntry):
        """
        Save a new log entry to the file.
        :param entry: LogEntry instance to save.
        """
        try:
            with open(self.file_path, 'r+') as file:
                # Load existing logs
                data = json.load(file)
                # Append new log entry
                data.append(entry.to_dict())
                # Write back to file
                file.seek(0)
                json.dump(data, file, indent=2)
        except FileNotFoundError:
            # Create a new file if it doesn't exist
            with open(self.file_path, 'w') as file:
                json.dump([entry.to_dict()], file, indent=2)

    def get_all_logs(self):
        """
        Retrieve all log entries from the file.
        :return: List of LogEntry instances.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [LogEntry.from_dict(entry) for entry in data]
        except FileNotFoundError:
            # Return an empty list if the file doesn't exist
            return []
