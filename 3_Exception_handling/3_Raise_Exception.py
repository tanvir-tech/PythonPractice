x = "hello"

try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")  # raising exceptions

except TypeError:
    print("type error")





