from os import path

if(not path.exists("newfile.txt")):

    file_obj = open("newfile.txt", "x")  # file creation -> x
    print("File created successfully")

    file_obj.write("Hello world")

    file_obj.close()
else:
    print("File creation failed!..........File already exists.")


