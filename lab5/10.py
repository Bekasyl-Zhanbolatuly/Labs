import re

txt = "camelCaseToSnakeCase"
x = re.sub(r"([A-Z])", r"_\1", txt).lower()
print(x)