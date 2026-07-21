import os

# folder = os.listdir(".")


for root, folder, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))