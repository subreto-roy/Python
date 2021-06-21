def exponent(x,y):
    if y==0:
        return 1
    else:
        return x*exponent(x,y-1)
print(exponent(2,3))
