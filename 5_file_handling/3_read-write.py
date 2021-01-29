try:
    file_obj= open("demofile.txt","r+")

    print(file_obj.read())                # full file
    file_obj.write("\nHello world")
    print(file_obj.read())                # full file


except:
    print("File not found !")
finally:
    file_obj.close()



