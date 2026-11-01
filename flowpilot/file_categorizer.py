#file_categorizer.py

from pathlib import Path

class FileCategorizer:
    def __init__(self, file_path):
            self.file_path = file_path
    extension_map = {".jpg":"Images",
                 ".png":"Images",
                 ".pdf":"Documents",
                 ".txt":"Text",
                 ".py":"Code",
                 ".mp3":"Audio",
                 ".mp4":"Videos"}
    def categorize(self):
        result = []
        for item in self.file_path:
            path_obj = Path(item)
            category = self.extension_map.get(path_obj.suffix.lower(), "Others")
            result.append((path_obj, category))
        return result