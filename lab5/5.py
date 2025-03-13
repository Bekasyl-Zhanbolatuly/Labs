import re

txt = "ak dmjf abbbbk kjajgfb allb"
x = re.findall(r"\b\w*a\w*b\b", txt)
print(x)