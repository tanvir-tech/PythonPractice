try:
    file_obj= open("demofile.txt","a")
    file_obj.write("\nAPPEND!")
    print("success")

except:
    print("File not found !")
finally:
    file_obj.close()


