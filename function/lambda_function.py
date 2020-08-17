# lambda *args : OneExpression


def multiplier(n):
    return lambda a:a*n

doubler = multiplier(2)   # using n
result = doubler(5)       # using a
print(result)


tripler = multiplier(3)   # using n
result = tripler(5)       # using a
print(result)
