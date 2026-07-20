import os

folder = os.listdir("files")

for item in folder:
    path = os.path.join("files", item)

    if os.path.isfile(path) and item.endswith(".txt"):
        print(item)