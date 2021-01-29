div = 0

try:
    a, b = map(int, input("Enter 2 Integer with space :").split())

    div = a/b
    print("Division is =", div, type(div))

except ZeroDivisionError as z:
    print("Can not divide by Zero",z)

except ValueError:
    print("ValueError!.....insert 2 integers only")

except:
    print("Other error")

finally:
    print("---------------File,Database,Socket are closed-----------")


