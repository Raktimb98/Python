import os

file_path = "D:/Programming/python/test.txt"

if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")