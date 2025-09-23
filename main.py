#password game
import random
reallist = []
for i in range(5):
    reallist.append(random.randint(0,9))
def printcorrect(g,r):
    output = ""
    for i in range(5):
        if reallist[i] == int(guesslist[i]):
            output+=f"{reallist[i]}✅ "
        elif int(guesslist[i]) in reallist:
            output+=f"{guesslist[i]}🟨 "
        else:
            output+=f"{guesslist[i]}❌ "
    return output
guess = input("Welcome to the hacker bank: Enter the hacked passcode (X X X X X): \n").strip()
gl = guess.split(" ")
guesslist = [int(x) for x in gl]
tries = 1
print(printcorrect(guesslist,reallist))
while not guesslist==reallist:
    guess = input("Enter the hacked passcode (X X X X X): \n").strip()
    gl = guess.split()
    guesslist = [int(x) for x in gl]
    tries +=1
    print(printcorrect(guesslist,reallist))
print(f"Congratulations! You got it and it took you {tries} tries!")

