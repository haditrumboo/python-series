import os

start_folder = "."

empty_folders = []
count = 0

for root, dirs, files in os.walk(start_folder):
    if len(dirs) == 0 and len(files) == 0:
        empty_folders.append(root)
        count += 1

if count > 0:
    print(f"Found {count} empty folder(s):")
    for folder in empty_folders:
        print(folder)
else:
    print("No empty folders were found.")