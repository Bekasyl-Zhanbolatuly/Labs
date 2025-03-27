import re

txt = "ba, fgdfh, gfhhhg, aaab, abb, abbbb"
x = re.findall(r"\b\w*ab{2,3}\b", txt)
print(x)