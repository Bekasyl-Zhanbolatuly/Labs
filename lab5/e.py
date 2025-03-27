import re

txt = "aj fhfgh abbd lagkbok adlb"
x = re.findall(r"\b\w*a\w*b\b", txt)
print(x)