import os

path = input("Enter Directory Path: ")


contents = os.listdir(path)

for item in contents:
    print(item)