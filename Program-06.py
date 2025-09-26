# This is a program to print the list of file and folder present inside the operating system.

import os

folder_path = input("Enter the folder path : ")

try:
    content = os.listdir(folder_path)

    print(f"The list of file and folder present inside the folder path {folder_path} is : ")

    for item in content:
        print(item)

except FileNotFoundError:
    print("The folder path is not found.")
except PermissionError:
    print("The folder path is not access.")
