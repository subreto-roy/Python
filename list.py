"""
q=[2,3,4]
print(q)

#sublist
q=[1,2,3,4,5,6]
print(q[0:5])

a=[1,2,3,4]
b=['x','y','z']
ab=a+b
print(ab)
x=['p','q','r']
new_x=x*3
print(new_x)

#delete
p=['a',0,9]
del p[0]
print(p)

places_visited=['India','Nepal','Malaysia','Bhutan','USA','bk']
#index() method
print(places_visited.index('Bhutan'))
#the append()
places_visited.append('Africa')
print(places_visited)
#insert
places_visited.insert(2,'United kingdom')
print(places_visited)
#the remove()
places_visited.remove('Nepal')
print(places_visited)
#the sort
places_visited.sort(key=str.lower)
print(places_visited)
#reverge sort
places_visited.sort(key=str.lower,reverse=True)
print(places_visited)

my_tech=['iphone','android']
print('Enter a tech name')
name=input()
if name not in my_tech:
    print('Nope its not in my list')
else:
    print(name+ 'is my tech')
"""
#Assuming multiple values at once
chocolate_milk_shake=['chocolate','milk','ice_cream','blender']
x,y,z,q=chocolate_milk_shake
print(x,y,z,q)
