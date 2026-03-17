import shutil
from pathlib import Path

root = Path(__file__).parent
removed = 0

for cache_dir in root.rglob("__pycache__"):
    shutil.rmtree(cache_dir)
    removed += 1

print(f"Removed {removed} __pycache__ director{'y' if removed == 1 else 'ies'}.")
