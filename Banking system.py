bank_users={'Alice':100,'samee':200,'robert':3000}
print('Welcome to bank')
while True:
    print('What do you like to do?')
    print(' '+'1.View Balance')
    print(' '+'2.View All Bank Info')
    print(' '+'3.Update Balance')
    print(' '+'4.Exit')

    desc=input()
    if desc=='1':
        print('Enter your Name,Please: ')
        k=input()
        if k in bank_users.keys():
            print(k +'Your Bank Balance is '+str(bank_users[k]))
        else:
            print("The User can not be found.Would you like to add the user to the account?")
            desc=input()
            if desc=='YES':
                k=input('Enter your name :')
                v=input('Enter your Balance :')
                bank_users.update({ k: v})
            else:
                print('Would like to exit?')
                desc=input()
                if desc=='YES':
                    break
    elif desc == '2':
        for k,v in bank_users.items():
            print('Username:'+str(k)+' Bank balance: '+str(v))
    elif desc == '3':
        print('Enter  your name: ')
        k=input()
        if k in bank_users.keys():
            print('Do you want to add or subtract from your savings?')
            desc=input()
            if desc=='ADD':
                temp=bank_users[k]
                extra=input('Enter the amount you want to add: ')
                bank_users[k]=temp+int(extra)
                print('Balance update.It is : ')
                print(bank_users[k])
            elif desc == 'Subtract':
                temp=bank_users[k]
                extra=input('Enter the amount you want to subtract: ')
                bank_users[k]=temp-str(extra)
                print('Balance update.It is: ')
                print(bank_users[k])
        else:
            print('There is no such account in the bank databse.')

    elif desc=='4':
        break







