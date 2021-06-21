#my_staff={'book': 'coorbook','phone':'iphone','home':'banladesh'}
#print(my_staff['book'])


#x={0:100,1:200,3:400}
#print(x[1])

#concatenation two dictionary
""""
D ={'a':100,'b':200}
E ={'c':300, 'd':400}

new_dic=D.copy()
new_dic.update(E)
print(new_dic)

identity={'Name': 'Ajwad','Age':'21','job':'student'}

#printing values
for i in identity.values():
    print(i)

#printing keys
for i in identity.keys():
    print(i)

for i in identity.items():
    print(i)

identity={'Name': 'Ajwad','Age':'21','job':'student'}

x=list(identity.keys())
y=list(identity.values())

print(x)
print(y)
"""
identity={'Name': 'Ajwad','Age':'21','job':'student'}

#A handy trick
#for k,v in identity.items():
    #('key: '+k+' value:'+v)
#use of 'in keyword

print('Name' in identity)
print('pop' in identity)
print('Akil' in identity.values())
print('Age' in identity.keys())


    #the get() method
print(str(identity.get('Name','Default')))
print(str(identity.get('Height','Default')))

#the  setdafault()
print(identity.setdefault('Name','cosmos'))
print(identity.setdefault('height','6ft'))
print(identity)




















