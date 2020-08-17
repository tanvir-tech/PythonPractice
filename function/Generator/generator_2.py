def generator():
    n=5
    yield n        # 1st next
    n*=n
    yield n        # 2nd next

obj = generator()

# print(next(obj))
# print(next(obj))
# print(next(obj)) # stop iteration exception

for x in obj:
    print(x)
