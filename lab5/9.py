import re

txt = "HelloWorldBigData"
x = re.sub(r"([A-Z])", r" \1", txt)
print(x)