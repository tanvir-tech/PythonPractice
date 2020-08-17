try:
    file_obj= open("newfile.txt","x")

    file_obj.write("new !")


except:
    print("File not found !")
finally:
    file_obj.close()


