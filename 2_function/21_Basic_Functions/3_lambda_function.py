# ( lambda *args : singleExpression ) (Actual_Inputs)

r=(lambda x:x*x)(5)                 # lambda called with 5
print("Simple lambda call => Square is =",r)



def lambda_Variable_Multiplier(n):
    return lambda a:a*n                  # lambda is incomplete => (n=?)..............a is the Input

doubler = lambda_Variable_Multiplier(2)  # (n=2) => completing lambda function in doubler variable
result = doubler(5)                      # doubler(5) => lambda(a) function called
print("Double is =",result)


tripler = lambda_Variable_Multiplier(3)  # (n=3) => completing lambda function in tripler variable
result = tripler(5)                      # tripler(5) => lambda(a) function called
print("Triple is =",result)
