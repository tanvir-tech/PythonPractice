# decorator
def div_Decorator(div):
    def wrapper(a,b):         # inner function with those variables
        if a<b:
            a,b = b,a
        return div(a,b)       # returning main function
    return wrapper            # returning inner function




# main function with Annotation of Decorator
@div_Decorator
def div(a,b):
    print("Division result : ",a/b)


div(2,4)      # calling the decorated main function
div(4,2)