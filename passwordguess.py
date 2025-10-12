#password game
import random
class passwordGame():
    
    def __init__(self):
        self.reallist = []
        self.tries = 0
        self.gameover = False
        self.message = "Welcome to the hacker bank! Enter the hacked passcode (X X X X X)."
    
    def start_game(self):
        # initialize fresh list each time a new game starts
        self.reallist = []
        for i in range(5):
            self.reallist.append(random.randint(0,9))
        self.tries = 0
        self.gameover = False
        self.message = "Game started! Enter 5 numbers separated by spaces. "
        return self.message
    def printcorrect(self, g):
        output = ""
        for i in range(5):
            if self.reallist[i] == int(g[i]):
                output+=f"{self.reallist[i]}✅ "
            elif int(g[i]) in self.reallist:
                output+=f"{g[i]}🟨 "
            else:
                output+=f"{g[i]}❌ "
        return output.strip()
    def makeguess(self,guess):
        if self.gameover:
            return f"Game over! The password was {''.join(map(str,self.reallist))}."
        try:
            guesslist = [int(x) for x in guess.split()]
            if len(guesslist) != 5:
                return "Invalid input! Please enter 5 numbers separated by spaces."
        except:
            return "Invalid input! Please enter numbers only."
        self.tries+=1
        feedback = self.printcorrect(guesslist)
        if guesslist == self.reallist:
            self.gameover=True
            return f"{feedback}\n CONGRATULATIONS! You cracked the code in {self.tries} tries!"
        else:
            return f"{feedback}\n Try again =("