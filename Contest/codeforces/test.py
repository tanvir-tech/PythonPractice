from math import ceil


n,m,a = map(int,input().split())


A = ceil(n/a)
print(A)

B = ceil(m/a)
print(B)

print(int(A*B))

