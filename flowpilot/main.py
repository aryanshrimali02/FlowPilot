#main.py

from file_scanner import FileScanner
from file_categorizer import FileCategorizer
from action_planner import ActionPlanner
from file_organizer import FileOrganizer

scanner = FileScanner(r"D:\VS Code\Python\GitProject\FlowPilot\sample_files")
files = scanner.scan()

categorizer = FileCategorizer(files)
results = categorizer.categorize()

print("FlowPilot - File Scan Results")
print("-"*30)
for filename, category in results:
    print(f"{filename.name} --> {category}")
print()

print("FlowPilot - Organization Preview")
print("-"*35)
planning = ActionPlanner(results ,r"D:\VS Code\Python\GitProject\FlowPilot\sample_files\organized_files")
action_plan = planning.plan()
for original_path, destination_path in action_plan:
    print(f"{original_path.name} --> {destination_path}")
print()

selection = input("Do you want to organize these files? (y/n): ").strip().lower()
if selection == "y":
    organizer = FileOrganizer(action_plan)
    summary = organizer.organize()
    print("Organization process completed.")
    print("Organization Summary".center(30,"="))
    print(f"Files moved: {summary['moved']}")
    print(f"Files skipped: {summary['skipped']}")
    print(f"Files failed: {summary['failed']}")
    print("="*30)
elif selection == "n":
    print("Operation cancelled. No files were moved.")
else:
    print("Invalid selection.")