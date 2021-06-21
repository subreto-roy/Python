import math
astr = input()
bstr = input()
cstr = input()

a=int(astr)
b=int(bstr)
c=int(cstr)
D = math.sqrt(b*b-4*a*c)
x1 = (-b+D)/(2*a)
x2=(-b-D)/(2*a)
print(x1)
print(x2)

