import re

txt = "a, Ndc, jDjd"
x = re.findall(r"[A-Z][a-z]+", txt)
print(x)