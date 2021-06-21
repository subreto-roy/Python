
contact_no={'sam':0000,'smith':1111,'Ron':9898}
x=0

while x<5:
    print('Enter your name')
    name=input()

    if name =='':
        break
    if name in contact_no:
        print('The contact  of '+name+' is '+str(contact_no[name]))
    else:
        print('There is so such name in the phone-book.Do you want to add it?')
        desc=input()

        if desc=='yes':
            print('Enter the Number:')
            num=input()
            contact_no[name]=num
            print('Dictionary Update.')
        elif desc=='no':
            print('Do you want to quit?')
            desc=input()
            if desc=='yes':
                break
            else:
                print('keep searchong.')

    x=x+1

