# factorial function
import sys
sys.setrecursionlimit(10000)


def factorial(n):
    print(n,end=" _ ")

    if (n == 0) :
        fact = 1
    else:
        fact = n+factorial(n-1)   # .........return value is used

    return fact            #........ ........must be used for recursion

result = factorial(1000)
print('')
print(result)

