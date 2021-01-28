#.......................................................................... function_defination
def odd_even(num):
    if num%2==0:
        print(num,"is Even")
    else:
        print(num,"is Odd")
#................................................................... xarg
def mathfunction(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n
    return sum
#..................................................................... xxarg
def function_2(**key_value):
    print(key_value)

#.......................................................................................................function call
odd_even(1000)
print("Sum is ",mathfunction(5,4,8,7))
function_2(id="it-18043",name="Tanvir")


