# [ "expression"  for  "variable"  in  "iterable"   if "condition"]


myTuple=(1,2,3,4,5)
squares = [x*x for x in myTuple]                    # list_comprehension
print("Squares are ",squares)



list = list(myTuple)
oddlist = [x for x in list if x%2!=0]                    # list_comprehension with condition
print("Odds are ",oddlist)


