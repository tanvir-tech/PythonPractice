import math as m

n,k = map(int,input("Enter numbers with space : ").split())

print("Minimum is : ",min(n,k))  # built-in
print("Maximum is : ",max(n,k))
print("Absolute value of n : ",abs(n))
print("n^k : ",pow(n,k))


print("Ceil of n : ",m.ceil(n))                                                         # math functions
print("Truncated of n : ",m.trunc(n))
print("Floor of n : ",m.floor(n))

print("Factorial is : ",m.factorial(n))
print("Permutation of n,k is :",m.perm(n,k))
print("Combination of n,k is :",m.comb(n,k))

print("Square root of n : ",m.sqrt(n))
print("e^k : ",m.exp(k))
print("Log of n, base k : ",m.log(n,k))
# so on............