import re

txt = "a, Abc, aBcbA"
x = re.findall(r"[A-Z][a-z]+", txt)
print(x)