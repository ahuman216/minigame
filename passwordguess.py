#password game
def passwordGame():
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
    while True:
        try:
            guess = input("Welcome to the hacker bank: Enter the hacked passcode! (X X X X X): \n").strip()
            gl = guess.split(" ")
            if len(gl)<=4:
                raise Exception
            guesslist = [int(x) for x in gl] 
            break

            
        except:
            print("Not a valid input, try again")
        
    tries = 1
    print(printcorrect(guesslist,reallist))
    while not guesslist==reallist:
        
        while True:
            try:
                guess = input("Enter the hacked passcode! (X X X X X): \n").strip()
                gl = guess.split(" ")
                guesslist = [int(x) for x in gl]
                if len(guesslist<5):
                    raise Exception
            except:
                print("Not a valid input, try again")
            break
        tries +=1
        print(printcorrect(guesslist,reallist))
    print(f"Congratulations! You got it and it took you {tries} tries!")
