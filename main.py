"""Write the out-of-office auto-reply entry to /output/entry.txt."""

from pathlib import Path

ENTRY = "I'm on vacation. Your email was auto-deleted by my out-of-office reply, which is the only part of me still working."

Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
