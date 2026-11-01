#file_organizer.py

import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, action_plan):
        self.action_plan = action_plan
    def organize(self):
        for original_path, destination_path in self.action_plan:
            destination_path = Path(destination_path)
            if destination_path.exists():
                print(f"skipping {destination_path.name}: destination Already exists")
                continue
            Path(destination_path).parent.mkdir(parents=True,exist_ok=True)
            shutil.move(original_path, destination_path)