import math

n = int(input("Input number of sides: "))
l = int(input("Input the lengh of a side: "))
A = (l**2 * n)/(4 * math.tan(math.pi/n))
print(f"The area of the polygon is:", A)