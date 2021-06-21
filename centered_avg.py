"""
def centered_average(some_list):
    sum=0
    count=0
    temp_list=some_list.sort()
    for i in range(1,len(some_list)-1):
        sum=sum+some_list[i]
        count=count+1
    return sum/count


a=[1,2,3,4,5]

print(centered_average(a))

import copy as cp
s=[10,20]
s.append(60)
n=cp.copy(s)
n.append(60)
x=cp.copy(n)
x.append(60)
print(s,n,x, sep='#')

"""
s=[1,2,3,4,5,6]
print(s[:-1])
print(s[-1:])
print(s.intersection[5])
