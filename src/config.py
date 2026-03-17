from pathlib import Path
import os


def get_data_path() -> Path:
    """
    Returns the platform-appropriate path for chat_log.json.
    Stored outside the repo in the OS user-data directory so it
    can never accidentally be committed to source control.

    Windows : %APPDATA%\\echobot\\chat_log.json
    Linux/Mac: ~/.local/share/echobot/chat_log.json
    """
    if os.name == 'nt':
        base = Path(os.environ.get('APPDATA', Path.home() / 'AppData' / 'Roaming'))
    else:
        base = Path(os.environ.get('XDG_DATA_HOME', Path.home() / '.local' / 'share'))
    data_dir = base / 'echobot'
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / 'chat_log.json'
