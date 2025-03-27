import re

txt = "snake_case_to_camel_case"
x = re.sub(r"_([a-z])", lambda v: v.group(1).upper(), txt)
print(x)