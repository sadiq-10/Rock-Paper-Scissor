import random

def play():

    user = input("what's your choice? Rock 'r', Paper 'p', or Scisser 's'?\n ")
    com = random.choice(["r", "p", "s"])

    if user == com:
        return "Its a tie"

    if win(user, com):
        return "you win"

    
    return "Computer win"


#r>s, s>p, p>r

def win(player, opponent):

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True


print(play())