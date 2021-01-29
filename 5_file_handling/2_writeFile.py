try:
    file_obj= open("demofile.txt","w")

    file_obj.write("Hi Tanvir Hello!\nWelcome to demofile.txt.\nThis file is for testing purposes.\nGood Luck!")
    print("success")

except:
    print("File not found !")
finally:
    file_obj.close()


