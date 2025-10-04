import passwordguess as pd
import rockpaperscissors as rp
games = ["rock paper scissors", "password hack"]
gamepick = str(input("Enter the game you want to play: rock paper scissors or password hack")).lower()
if gamepick in games:
    if gamepick =="rock paper scissors":
        rp.rpsgame()
    elif gamepick =="password hack":
        pd.passwordGame()
else:
    print("Invalid input")
