try:
    file_obj= open("demofile.txt","w")

    file_obj.write("Hi Tanvir Hello!\n Welcome to demofile.txt.\nThis file is for testing purposes.\n Good Luck!")


except:
    print("File not found !")
finally:
    file_obj.close()


