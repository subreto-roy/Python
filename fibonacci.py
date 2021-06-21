def fibonacci(n):
    if n==0:
        return 0
    else:
        x=0
        y=1
        print(x)
        print(y)
        for i in range(1,n):
            z=x+y
            x=y
            y=z
            print(z)


fibonacci(3)
