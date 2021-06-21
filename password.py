password_bank={'sam':1234,'smith':9999}

matched=False
x=0

print('Enter your Name')

while x<5:
    name=input()
    if name in password_bank:
        for i in range(0,3):
            print('Enter Your Password')
            password=input()
            if int(password) in password_bank.values():
                matched=True
                print('Access granted.')
                break
            else:
                print('Wrong password.Enter Again:'+'You Have'+str(2-i)+'tries left')
    else:
        print('There is no such name in the password_bank.try again')

    x=x+1

    if matched:
        break
