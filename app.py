from flask import Flask, render_template, request, jsonify
import subprocess
from passwordguess import passwordGame
from rockpaperscissors import rockPaperScissors
from hangman import HangmanGame


app = Flask(__name__)
password_game = passwordGame()
rps_game = rockPaperScissors()
hangman_game = HangmanGame()

@app.route('/')
def home():
    return render_template('index.html')
#password hack
@app.route('/start-password-game', methods = ['POST'])
def startpasswordgame():
    message = password_game.start_game()
    return jsonify({"message": message})
@app.route('/guess-password', methods = ['POST'])
def guesspassword():
    guess= request.json.get('guess')
    # passwordGame class defines method makeguess (lowercase g)
    message = password_game.makeguess(guess)
    return jsonify({"message":message})

#rock paper scissor
@app.route('/start-rps-game', methods = ['POST'])
def start_rps_game():
    message = rps_game.start_game()
    return jsonify({"message":message})
@app.route('/play-rps', methods = ['POST'])
def play_rps():
    choice = request.json.get('choice')
    # rockPaperScissors class defines makemove (no underscore)
    message = rps_game.makemove(choice)
    return jsonify({"message": message})

#hangman
@app.route('/start-hangman-game', methods = ['POST'])
def start_hangman_game():
    message = hangman_game.start_game()
    return jsonify({"message":message})
@app.route('/guess-hangman', methods = ['POST'])
def guess_hangman():
    letter = request.json.get('letter')
    # HangmanGame exposes makeguess (lowercase, no underscore)
    message = hangman_game.makeguess(letter)
    return jsonify({"message":message})

if __name__ == '__main__':
    app.run(debug=True)