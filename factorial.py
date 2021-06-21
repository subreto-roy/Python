def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=input()
print(fact(int(n)))
