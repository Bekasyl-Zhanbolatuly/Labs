import re

a = "a, Abb, AG, Aa"
x = re.findall(r"[A-Z][a-z]", a) 
print(x)