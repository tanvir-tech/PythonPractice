a,b = map(int,input().split())
div = 0

try:
    div = a/b

except ZeroDivisionError as z:
    print("b can not be Zero",z)

else :
    print("No ZeroDivisionError")

finally:
    print("Division is ",div)
    print("In the finally block file,database,socket are closed")

