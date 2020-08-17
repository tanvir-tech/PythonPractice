from math import ceil

n,m,a=map(int,input().split())


tile_wide = ceil(n/a)
tile_long = ceil(m/a)


print(int(tile_wide * tile_long))

