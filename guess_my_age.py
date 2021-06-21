import random as r
secrect_age=r.randint(1,10)
flag=False
def game_func(guessed_age,secret):
    if guessed_age<secret:
        return 'TOO LOW'
    elif guessed_age>secret:
        return 'TOO HIGH'
    else:
        return 'CORRECT'
for i in range(1,6):
    print('Take a guess.you have '+str(6-i)+' guesses left.')
    guess=input()
    if game_func(int(guess),secrect_age)=='CORRECT!':
        print('YOU WON THE GAME!')
        flag=True
        break
if not flag:
    print("YOU LOST THE GAME!")
