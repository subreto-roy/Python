def area_func():
    print('Enter the shape to find the area:')
    shape=input()
    if shape=='circle':
        print("please enter the radius:")
        r=float(input())
        area=3.1416*r*r
        print('the area is: ')
        print(area)
    elif shape=='triangle':
        print('plase enter the base:')
        base=float(input())
        print('please enter the height:')
        height=float(input())
        area=0.5*base*height
        print(area)

    elif shape=='rectangle':
        print('enter length:')
        length=float(input())
        print('enter the width:')
        width=float(input())
        area=length*width
        print(area)
    elif shape=='square':
        print('enter length')
        len=float(input())
        area=len**2
        print(area)
    elif shape=='trapezium':
        print('enter the side')
        s1=float(input())
        s2=float(input())
        s3=float(input())
        h=float(input())
        area=0.5*(s1+s2+s3)*h
        print('area')
area_func()
