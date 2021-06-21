row=int (input())

count=0
for i in range (0,row):
    for j in range(0,row-i-1):
        print(end=" ")
    count=count+1
    for k in range(0, i+count):
        print("*", end= "")

    print(" ")
