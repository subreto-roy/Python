"""

def outer(message):
    print('In the outer function')

    def inner():
        print('Calling the inner functions ')
        print(message)

    return inner()

f=outer("hello world")
"""
def decorator(orginal_func):
    print("In the decorator functions\n")

    def wrapper():
        print(f'wrappper excuted before {orginal_func.__name__}()')

        if 10>5:
            print('yes it is true')

        return orginal_func()

    return wrapper

@decorator
def print_somethings():
    print('print_somethings is beign ran!')

print_somethings()



#using decorator in one way
#decorated_f= decorator(print_somethings)
#decorated_f()

#non keyword arguments=> f(1,2,3,4)
#keyword arguments => f(a=1,b=2,c=3)


def decorator2(orginal_func):
    print("In the decorator2 functions\n")

    def wrapper(*args,**kwargs):
        print(f'wrappper excuted before {orginal_func.__name__}()')

        if 10>5:
            print('yes it is true')

        return orginal_func()

    return wrapper


@decorator
def print_somethings():
    print('print_somethings is beign ran!')

#print_somethings()

@decorator2
def print_somethings_more(arg1,arg2):
    print(f'printing argument_1={arg1} and argumnt_2={arg2}')

print_somethings_more(1,2)




















