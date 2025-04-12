file_path = "python/test.txt"
try:
    with open(file_path,"r")as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")

except PermissionError:
    print(f"You do not have Permission to read: {file_path} this file")