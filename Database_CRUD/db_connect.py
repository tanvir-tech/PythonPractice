import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="ict-15")
mycursor = mydb.cursor()

mycursor.execute("select* from contact")

for i in mycursor:
    print(i)


mydb.disconnect()



