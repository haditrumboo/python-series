import os

folder = "."

empty_folders = []

for root, dirs, files in os.walk(folder):
    if not dirs and not files:
        empty_folders.append(root)

if empty_folders:
    print("Empty folders found:")
    for folder in empty_folders:
        print(folder)
else:
    print("No empty folders found.")