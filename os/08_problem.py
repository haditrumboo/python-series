import os

print("Current Working Directory:")
print(os.getcwd())

print("\nFiles and Folders:")
for item in os.listdir():
    print(item)

print("\nOperating System:")
print(os.name)

print("\nEnvironment Variables:")
for key, value in list(os.environ.items())[:5]:
    print(f"{key} = {value}")