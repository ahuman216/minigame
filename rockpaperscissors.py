import random
class rockPaperScissors:
    def __init__(self):
        self.playerscore = 0
        self.compscore = 0
        self.rounds = 0
        self.gameover = False
        self.message = "Let's play Rock Paper Scissors! First to 3 wins."
    def start_game(self):
        self.playerscore=0
        self.compscore=0
        self.rounds = 0
        self.gameover=False
        self.message = "Game started! Choose rock, paper or scissors!"
        return self.message
    def computerturn(self):
        num = random.randint(1,3)
        return ["Rock", "Paper", "Scissors"][num-1]
    def whowins(self, comp, player):
        if (comp ==player):
            return "It's a tie!"
        if comp =="Rock":
            return "You win this round!" if player=="Paper" else "The computer wins this round!"
        if comp == "Paper":
            return "You win this round!" if player =="Scissors" else "The computer wins this round!"
        if comp == "Scissors":
            return "You win this round!" if player == "Rock" else "The computer wins this round!"
    def makemove(self, playerchoice):
        if self.gameover:
            return "Game over! Start a new game."
        playerchoice = playerchoice.capitalize()
        if playerchoice not in ["Rock", "Paper", "Scissors"]:
            return "Invalid choice. Pick rock paper or scissors"
        compchoice = self.computerturn()
        winner = self.whowins(compchoice, playerchoice)
        if winner =="You win this round!":
            self.playerscore+=1
        elif winner == "The computer wins this round!":
            self.compscore+=1
        self.rounds+=1
        if self.playerscore==3 or self.compscore==3:
            self.gameover=True
            if self.playerscore==3:
                return f"{winner}\n You won after {self.rounds} rounds!"
            else:
                return f"{winner}\n The computer won after {self.rounds} rounds!"
        return f"{winner}\n Your score: {self.playerscore}, Computer score: {self.compscore}, Rounds: {self.rounds}"
        
"""         playerscore = 0
        compscore = 0
        rounds = 0


        def playerturn():
            personpick = ""
            print("Let's play rock paper scissors!")
            while True:
                    try:
                        num = int(input("Enter 1 for rock, 2 for paper, 3 for scissors "))
                        if num==1:
                            personpick = "Rock"
                        elif num==2:
                            personpick = "Paper"
                        elif num==3:
                            personpick = "Scissors"
                        else:
                            raise Exception
                        break
                    except:
                        pass
            return personpick

        def computerturn():
            num = random.randint(1,3)
            if num==1:
                comppick = "Rock"
            elif num==2:
                comppick = "Paper"
            elif num==3:
                comppick = "Scissors"
            return comppick

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
            print(f"The number of rounds we played is {rounds}!\n")
            
        if compscore==3:
            print("The computer won after ",rounds, "rounds!")
        else:
            print("You won after", rounds,"rounds!")

 """