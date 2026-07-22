import os

largest_size = 0
largest_file = ""

for root, folders, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            path = os.path.join(root, file)
            size = os.path.getsize(path)

            if size > largest_size:
                largest_size = size
                largest_file = path

print(f"Largest file: {largest_file}")
print(f"Size: {largest_size} bytes")



