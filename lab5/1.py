import re

txt = "ab, hdh, hdsggch, cabb, abbbb, abbb"
x = re.findall(r"\b\w*ab*\b", txt)
print(x)