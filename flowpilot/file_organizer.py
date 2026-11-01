#file_organizer.py

import shutil
import logging
from pathlib import Path

class FileOrganizer:
    def __init__(self, action_plan):
        self.action_plan = action_plan

    def organize(self):
        files_moved = 0
        files_skipped = 0
        files_failed = 0
        for original_path, destination_path in self.action_plan:
            destination_path = Path(destination_path)
            original_path = Path(original_path)
            if destination_path.exists():
                files_skipped += 1
                logging.warning(f"skipped {destination_path.name}: destination Already exists")
                continue
            try:
                destination_path.parent.mkdir(parents=True,exist_ok=True)
                shutil.move(original_path, destination_path)
                logging.info(f"Moved: {original_path.name}")
                files_moved += 1
            except FileNotFoundError as error:
                logging.error(f"{original_path.name} source file not found. Details: {error}")
                files_failed += 1
            except PermissionError as error:
                logging.error(f"Permission denied while organizing {original_path.name}. Details: {error}")
                files_failed += 1
            except OSError as error:
                logging.error(f"system ran into error while organizing {original_path.name}. Details: {error}")
                files_failed += 1
        summary = {
            "moved": files_moved,
            "skipped": files_skipped,
            "failed": files_failed
        }
        return summary