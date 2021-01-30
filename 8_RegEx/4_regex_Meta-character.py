import re

pattern = r"c[o]l.r"
text = "My favourite color is Green.Green is the color of nature."


search_Obj = re.search(pattern, text)
if search_Obj:
    print("String founded")
    print(search_Obj.start())
    print(search_Obj.end())
    print(search_Obj.span())
else:
    print("String not found")

"""
Metacharacters

[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any single character (except newline character)	"he..o"	

^	Starts with	"^hello"	
$	Ends with	"world$"	

*	(0 -> more) occurrences	"aix*"	
+	(1 -> more) occurrences	"aix+"	
?   (0 -> 1) occurrences	"aix?"	
{}	Exactly the specified number of occurrences	"al{2}"	

|	Either or	"falls|stays"	
()	Capture and group

"""