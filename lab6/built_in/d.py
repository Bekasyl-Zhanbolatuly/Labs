import time
import math

num = int(input())
ms = int(input())

time.sleep(ms / 1000) 

res = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {res}")  