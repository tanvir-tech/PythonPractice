#1+2+3+4+5+.......+n
#recursion

def tri_recursion(k):
  if(k > 0):                                        # recursive case
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0                                     # base case
  return result





#function call
print("\n\nRecursion Example Results")
tri_recursion(6)