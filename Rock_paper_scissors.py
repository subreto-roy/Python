print("what do you want to choose?rock,paper or scissors?")
p1=input()
print("what do you want to choose?rock,paper or scissors?")
p2=input()
def game(a,b):
    if a== b:
        return "it is a tie!"
    elif a == 'rock':
        if b== 'scissors':
            return "Rock beats scissors!"
        else:
            return "paper beats rock!"
    elif a == 'scissors':
        if b == 'paper':
            return "Scissors beat paper!"
        else:
            return "Rock beats scissors!"
    elif a=='paper':
        if b == 'rock':
            return "paper beats rock!"
        else:
            return "Scissors beat paper!"
    else:
        return "You have not entered rock,paper or scissors"


print(game(p1,p2))
