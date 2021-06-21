import copy as cp

def f(some_list):
    some_list.append('ok')
x=[1,2,3]
s=cp.copy(x) #a copy of the list is made
f(s)
print(x)
