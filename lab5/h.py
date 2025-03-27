import re

txt = "HelloWorld BigData"
x = re.findall(r"[A-Z][a-z]*", txt)
print(x)