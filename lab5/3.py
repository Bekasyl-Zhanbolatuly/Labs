import re

txt = "a_b h_dh hdsgg_ch cab_b abb_bb abbb"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)