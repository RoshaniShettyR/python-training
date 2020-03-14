import re
str="utta7m"
pattern=re.compile('\d')
matches=pattern.finditer(str)
for match in matches:
    print(match)