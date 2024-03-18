import os

def check_file():
    file_name = "drivers.txt"
    if os.path.exists(file_name):
        print("Yaaay! I am working! :)")
    else:
        print(f"The file '{file_name}' does not exist.")

check_file()