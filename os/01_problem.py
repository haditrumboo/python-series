import os

folder = os.listdir("file")
count = 0

for item in folder:
    path = os.path.join("file", item)

    if os.path.isfile(path):
        print(item)
        count += 1

print(f"Total files: {count}")