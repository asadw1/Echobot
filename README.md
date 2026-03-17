# EchoBot

**EchoBot** is a local, offline chatbot companion that remembers past conversations to help you maintain context. It stores conversation summaries in a structured format and provides an easy way to retrieve them. The project is designed with extensibility in mind, utilizing a modular structure and clean design patterns.

---

## Features

- **Conversation Summaries:** Log and retrieve summaries of your conversations for easy reference.
- **Local Storage:** All data is stored offline in a JSON file for privacy and security.
- **Command-Line Interface (CLI):** User-friendly CLI to add summaries and view past conversations.
- **Modular Design:** Built using clean architecture principles to support future enhancements.

---

## Project Structure

```
echobot/
├── README.md               # Project documentation
├── setup.py                # For packaging and distribution (if needed)
├── requirements.txt        # List of dependencies
├── src/                    # Source code
│   ├── main.py             # Application entry point
│   ├── config.py           # Configuration settings
│   ├── models/             # Data models
│   │   └── log_entry.py    # Data model for conversation logs
│   ├── storage/            # Data storage and retrieval
│   │   └── log_repository.py  # Handles saving and retrieving logs
│   ├── services/           # Core application logic
│   │   └── summarizer.py   # Handles summarization and retrieval tasks
│   ├── utils/              # Utility functions
│   │   └── logger.py       # Logging utilities (optional)
│   └── views/              # User interface
│       └── cli.py          # Command-line interface
└── tests/                  # Unit tests
    └── test_log_repository.py  # Tests for the log repository
```

---

## Prerequisites

Make sure you have the following installed:

- **Python 3.8 or later**
- **pip** for dependency management

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/echobot.git
    cd echobot
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run EchoBot:**

    ```bash
    python run.py
    ```

---

## Usage

### Add a Conversation Summary

1. Run the CLI:

    ```bash
    python run.py
    ```

2. Select **Option 1** from the main menu.
3. Paste or type your conversation summary (for example, a summary of your current chat).
4. Confirm that the summary was saved (EchoBot will display a "Summary saved successfully!" message).

### View Recent Summaries

1. Run the CLI:

    ```bash
    python run.py
    ```

2. Select **Option 2** from the main menu.
3. When prompted, enter the number of recent summaries you would like to view.
4. The CLI will display the requested summaries along with their timestamps.

---

## Scripts

| Script | Command | Description |
|---|---|---|
| Run EchoBot | `python run.py` | Start the CLI |
| Clean cache | `python clean.py` | Recursively delete all `__pycache__` folders |

---

## Future Enhancements

Planned improvements for EchoBot include:

- **Search Functionality:** Allow users to search summaries by keywords or date ranges.
- **Graphical Interface (GUI):** Develop a user-friendly GUI to replace or complement the CLI.
- **Data Security Enhancements:** Add encryption for secure local storage.
- **Voice Integration:** Implement speech-to-text functionality for adding conversation summaries.

---

## Contributing

Contributions are welcome! If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Changelog

### [2026-03-17]

#### Added
- `echobotSummaryId` auto-incremented integer field added to every log entry; IDs are assigned by `LogRepository` on save and persisted in `chat_log.json`.
- `totalSummaryCount` root node added to `chat_log.json`; updated atomically on every write to always reflect the total number of summaries stored.
- Two new unit tests in `tests/test_log_repository.py`: `test_auto_increment_ids` and `test_total_summary_count`.
- `run.py` root-level entry point — run the app with `python run.py` instead of `python -m src.views.cli`.
- `clean.py` utility script — recursively removes all `__pycache__` directories from the project with `python clean.py`.

#### Changed
- `chat_log.json` structure migrated from a bare array to a root object `{ "totalSummaryCount": N, "entries": [...] }`; all existing entries backfilled with sequential `echobotSummaryId` values (1–end).
- `LogRepository` refactored to use `_read_store()` / `_write_store()` helpers, replacing the previous `r+` / `seek(0)` pattern that could corrupt the file on a shorter write.
- `LogEntry.from_dict()` uses `.get("echobotSummaryId", 0)` for safe backwards-compatible deserialization.

#### Fixed
- Missing `from datetime import datetime` import in `tests/test_log_repository.py` that caused a `NameError` when running the test suite.
- `chat_log.json` and `chat_log.json.bak` added to `.gitignore` to prevent local conversation data from being committed to source control.

---

Happy coding and enjoy building with EchoBot!
