f=open('Number','w+')
f.write('123321')
f.close()

f=open('Number','r+')
some_list=list(f.read())
f.close()
is_palindrome=True


for i in range(int(len(some_list)/2)):
    if some_list[i]!=some_list[len(some_list)-i-1]:
        is_palindrome=False

if is_palindrome:
    f=open('Number','a')
    f.write('Y')
    f.close()
else:
    f=open('Number','w')
    for i in range(len(some_list)):
        f.write('0')

