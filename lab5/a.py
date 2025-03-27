import re

txt = "ab, thr, ptih, abccb, babab, ababab"
x = re.findall(r"\b\w*ab*\b", txt)
print(x)