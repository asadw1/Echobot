import unittest
import os
from src.models.log_entry import LogEntry
from src.storage.log_repository import LogRepository

class TestLogRepository(unittest.TestCase):
    def setUp(self):
        """Set up a temporary test file."""
        self.test_file = 'test_chat_log.json'
        self.repository = LogRepository(self.test_file)

    def tearDown(self):
        """Clean up the test file."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_log_and_retrieve_logs(self):
        """Test saving and retrieving logs."""
        entry1 = LogEntry(timestamp=datetime.now(), summary="First test log.")
        entry2 = LogEntry(timestamp=datetime.now(), summary="Second test log.")
        
        # Save logs
        self.repository.save_log(entry1)
        self.repository.save_log(entry2)
        
        # Retrieve logs
        logs = self.repository.get_all_logs()
        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[0].summary, "First test log.")
        self.assertEqual(logs[1].summary, "Second test log.")

if __name__ == '__main__':
    unittest.main()
