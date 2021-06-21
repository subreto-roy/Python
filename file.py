"""#open a file
f=open('a.txt','w')

#getting some info
print('name= ',f.name)
print('is it closed? ',f.closed)
print('mode =',f.mode)
f.write('python is my favorite langauge.')
f.close()

#appending to a file
f=open('a.txt','a')
f.write('I also love Java')
f.close()

#r+ functionality
f=open('a.txt','r+')
info=f.read()
print(info)
f.close()
"""
#w+ mode
f=open('a.txt','w+')
f.write('All is lost!')
f.close()

