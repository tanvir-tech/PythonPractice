import re

pattern = r"color"
text = "My favourite color is Green.Green is the color of nature."

print(text)

text_2 = re.sub(pattern,"colour",text)
print(text_2)

text_3 = re.sub("Green","Black",text_2,count=1)
print(text_3)
