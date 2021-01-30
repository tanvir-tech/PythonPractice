import re

pattern = r"color"

if re.match(pattern,"color is first word"):
    print("Matched")
else:
    print("Not matched")

if re.search(pattern,"Red is a color"):
    print("Searched pattern found")
else:
    print("Searched pattern not found!")

foundList = re.findall(pattern,"Red is a color.Other colors are not red")
print(foundList)
