import passwordguess as pd
import rockpaperscissors as rp
import hangman as hm
games = ["rock paper scissors", "password hack", "hangman"]
gamepick = str(input("Enter the game you want to play: rock paper scissors or password hack")).lower()
if gamepick in games:
    if gamepick =="rock paper scissors":
        rp.rpsgame()
    elif gamepick =="password hack":
        pd.passwordGame()
    elif gamepick == "hangman":
        hm.hangman()

else:
    print("Invalid input")
