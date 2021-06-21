"""
print('hello',end='')
print('world')


print('a','b','c',sep=',')

#Example of scopes
def f():
    c=10
    print(c)
f()

#example 2
def function():
    global a
    print(a+23)
a=10
function()
"""
#example 3
#exception handling
def func(x):
    try:
        return 100/x
    except:
        return 'There is a zero division error'
answer=func(0)
print(answer)

