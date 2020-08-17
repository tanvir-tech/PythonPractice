#multiline string
ms = """multiline 
string"""
print(ms)


#multiplied
s = "123456789-" *5
print("Multiplied : "   ,s)


#slice
print("Sliced     : "       ,s[1:7])
print("Negatively sliced : "  ,ms[-1])


#format
x,y=5,10
text = "Integer is = {x1} Decimal is = {y1} and String is = {ms1}".format(x1=x,y1=y,ms1=ms)
print("formated   : "       ,text)

#format in easy way
print(f"Integer is = {x} Decimal is = {y} and String is = {ms}")
