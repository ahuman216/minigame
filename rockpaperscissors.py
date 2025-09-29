import random
playerscore = 0
compscore = 0
rounds = 0


def playerturn():
    personpick = ""
    print("Let's play rock paper scissors!")
    num = int(input("Enter 1 for rock, 2 for paper, 3 for scissors "))
    if num==1:
        personpick = "Rock"
    elif num==2:
        personpick = "Paper"
    elif num==3:
        personpick = "Scissors"
    return personpick

def computerturn():
    num = random.randint(0,3)
    if num==1:
        personpick = "Rock"
    elif num==2:
        personpick = "Paper"
    elif num==3:
        personpick = "Scissors"
    return personpick

def whowins(c, p):
    output = ""
    if c==p:
        output = "It's a tie!"
    if c=="Rock":
        if p=="Paper":
            output = "You win this round!"
        elif p == "Scissors":
            output = "The computer wins this round!"
    elif c=="Paper":
        if p =="Rock":
            output = "The computer wins this round!"
        elif p == "Scissors":
            output = "You win this round!"
    elif c=="Scissors":
        if p == "Rock":
            output = "You win this round!"
        elif p=="Paper":
            output = "The computer wins this round!"

    return output

while playerscore<3 and compscore<3:
    player = playerturn()
    comp = computerturn()
    winner = whowins(comp, player)
    print(winner)

    if winner=="You win this round!":
        playerscore+=1
    elif winner =="The computer wins this round!":
        compscore+=1
    print("Your score is ",playerscore, "and the computer's score is",compscore)
    rounds+=1
    print("The number of rounds we played is", rounds,"\n!")
    
if compscore==3:
    print("The computer won after ",rounds, "rounds!")
else:
    print("You won after", rounds,"rounds!")

