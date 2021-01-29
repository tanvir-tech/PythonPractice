try:
    file_obj= open("demofile.txt","r")

    print(file_obj.read())                # full file
    # print(file_obj.read(30))              # index wise
    # print(file_obj.readline())            # single line
    # print(file_obj.readline(3))            # single line 3
    # print(file_obj.readlines())            # single lines seperately

except:
    print("File not found !")
finally:
    file_obj.close()



