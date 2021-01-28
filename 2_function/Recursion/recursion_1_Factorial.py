# factorial function
import sys
sys.setrecursionlimit(10000)

def factorial(n):
    print(n,end="*")

    if (n == 0) :
        return 1   # ................................base case
    else:
        return n*factorial(n-1)   # .................recursive case


result = factorial(4)
print('')
print(result)
