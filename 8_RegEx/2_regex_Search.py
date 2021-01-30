import re

pattern = r"color"
text = "My favourite color is green"

search_Obj = re.search(pattern, text)

if search_Obj:
    print(search_Obj.start())
    print(search_Obj.end())
    print(search_Obj.span())




