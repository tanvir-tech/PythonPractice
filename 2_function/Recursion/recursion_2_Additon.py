#1+2+3+4+5+.......+n
#recursion

def tri_recursion(k):
  print(k,end="+")

  if(k > 0):
    return k + tri_recursion(k-1)                # recursive case
  else:
    return 0                                     # base case


#function call
print("Recursion Example Result :")
result = tri_recursion(6)
print("\nSeries Sum =",result)