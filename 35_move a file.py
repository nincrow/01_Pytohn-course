import os

source = "C:\\Users\\Angel Poveda\\Desktop\\test_1.1.txt"
destination = "test_1.1.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print (source+" was moved")
except FileNotFoundError:
    print(source+" was not found")