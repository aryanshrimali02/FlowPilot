#file_scanner.py

from pathlib import Path

class FileScanner:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def scan(self):
        files = []
        if not self.folder_path.exists() or not self.folder_path.is_dir():
            print("Folder Path invalid")
            return []

        for item in self.folder_path.iterdir():
           if not item.is_file():
               continue
           files.append(item)
        return files