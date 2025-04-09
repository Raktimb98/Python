txt_data = "I am learning Python.\n"
file_path = "python/test.txt"
with open(file= file_path, mode= "w") as file:
    file.write(txt_data)
    print("File written successfully.")