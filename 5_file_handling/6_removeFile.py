import os

try:
    os.remove("newfile.txt")
    print("File deleted")
except:
    print("Failed to remove!..........File doesn't exists")

