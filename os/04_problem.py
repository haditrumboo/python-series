# import os

# for root, folders, files in os.walk("practice"):
#     print(root)
#     print(folders)
#     print(files)
#     print("----------------")

import os

for root, folders, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))