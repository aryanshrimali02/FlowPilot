import hashlib
from pathlib import Path

class DuplicateDetector:
    def __init__(self, files):
        self.files = files
    def calculate_hash (self, file_path):
        hash_object = hashlib.sha256()
        file_path = Path(file_path)

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_object.update(chunk)

        return hash_object.hexdigest()
    def find_duplicates(self):
        duplicates = {}
        filtered_duplicates = {}

        for file_path in self.files:
            file_hash = self.calculate_hash(file_path)

            if file_hash not in duplicates:
                duplicates[file_hash] = [Path(file_path)]
            else:
                duplicates[file_hash].append(Path(file_path))
        for key, files in duplicates.items():
            if len(files) > 1:
                filtered_duplicates[key] = files

        return filtered_duplicates