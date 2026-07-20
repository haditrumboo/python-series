import os

folders = os.listdir()
count = 0

for item in folders:
    path = os.path.join(".", item)

    if os.path.isdir(path):
        print(item)
        count += 1

print(f"Total folders: {count}")