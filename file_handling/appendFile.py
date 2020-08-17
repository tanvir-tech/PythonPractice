try:
    file_obj= open("newfile.txt","a")

    file_obj.write("APPEND !!!")


except:
    print("File not found !")
finally:
    file_obj.close()


