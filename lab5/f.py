import re

txt = "hello world.hello, world"
x = re.sub(r"[ ,.]", ":", txt)
print(x)