import time
import math
num = int(input())
ms = int(input())
seconds = float(ms / 1000)
time.sleep(seconds)
res = math.sqrt(num)
print(f"Square root of {num} after {ms}  miliseconds is {res}")