import os

latest_file = ""
latest_time = 0

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)
        modified_time = os.path.getmtime(path)

        if modified_time > latest_time:
            latest_time = modified_time
            latest_file = path

print("Most recently modified file:")
print(latest_file)