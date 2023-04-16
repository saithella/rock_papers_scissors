import random

def play():
    user=input("Enter your choice ,R for rocks, S for scissors, P for paper: ")
    computer=random.choice(['R','P','S'])

    if user==computer:
        return 'tie'
    if is_win(user,computer):
        return 'You won'
    return 'You lose'

def is_win(player,opponent):
     if (player=='R' and opponent=='S') or (player=='P' and opponent=='R') or (player=='S' and opponent=='P'):
        return True


x=play()
print(x)