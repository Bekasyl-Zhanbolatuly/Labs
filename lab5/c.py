import re

txt = "a_c g_hg dsg_hch cfd_b ab_ba abb"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)