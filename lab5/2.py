import re

txt = "ab, hdh, hdsggch, cabb, abbbb, abbb"
x = re.findall(r"\b\w*ab{2,3}\b", txt)
print(x)