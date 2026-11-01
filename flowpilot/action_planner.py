#action_planner.py

from pathlib import Path

class ActionPlanner:
    def __init__(self, categorized_files, target_folder):
        self.categorized_files = categorized_files
        self.target_folder = Path(target_folder)
    def plan(self):
        plans = []
        planned_destinations = set()
        for file_path, category in self.categorized_files:
            destination = self.target_folder / category / file_path.name
            if destination in planned_destinations or destination.exists():
                print(f"skipping {file_path.name}: destination Already exists")
                continue
            plans.append((file_path, destination))
            planned_destinations.add(destination)
        return plans