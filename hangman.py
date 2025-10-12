from wonderwords import RandomWord
class HangmanGame:
    def __init__(self):
        self.hgstep = hgstep = [
    '''------
    |    |
    |
    |
    |
    |
    |
    ---------------''', 
    '''------
    |    |
    |   ( )
    |
    |
    |
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |    |
    |    |
    |
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |    |/
    |    |
    |   
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   /
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   / \\
    |
    ---------------''']
        self.word = ""
        self.wordlist = []
        self.guessedlist = []
        self.errornum=0
        self.gameover = False
        self.message = "Welcome to Hangman! Start a new game."
    def start_game(self):
        r = RandomWord()
        self.word = r.word()
        self.wordlist=list(self.word)
        self.guessedlist= ["_ "]*len(self.word)
        self.errornum = 0
        self.gameover = False
        self.message = f"Game started! Word length {len(self.word)}. Guess a letter."
        return self.message
    def makeguess(self, letter):
        if self.gameover:
            return f"Game over. The word was {self.word}"
        if not letter.isalpha() or len(letter)!=1:
            return "Invalid input! Enter a single letter!"
        letter = letter.lower()
        output = self.hgstep[self.errornum]+"\n"
        if letter in self.wordlist:
            for i in range(len(self.wordlist)):
                if self.wordlist[i] ==letter:
                    self.guessedlist[i]=letter
            output+= " ".join(self.guessedlist)+"\n"
            if self.wordlist==self.guessedlist:
                self.gameover=True
                return output + f"You did it! The word was {self.word}"
            return output+" Correct guess!"
        else:
            if self.errornum ==6:
                self.gameover=True
                return output + f"You DIED! The word was {self.word}"
            else:
                self.errornum+=1
                output = self.hgstep[self.errornum]+"\n"+ " ".join(self.guessedlist)+ "\n"
                return output


"""def hangman():
    
    from wonderwords import RandomWord
    hgstep = [
    '''------
    |    |
    |
    |
    |
    |
    |
    ---------------''', 
    '''------
    |    |
    |   ( )
    |
    |
    |
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |    |
    |    |
    |
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |    |/
    |    |
    |   
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   /
    |
    ---------------''',
    '''------
    |    |
    |   ( )
    |   \|/
    |    |
    |   / \\
    |
    ---------------''']
    def printlist(l):
        output=""
        for item in l:
            output+=item
        print(output)
    r = RandomWord()
    word = r.word()
    wordlist = []
    guessedlist = []
    errornum = 0
    for i in range(len(word)):
        guessedlist.append("_ ")
    for i in range(len(word)):
        wordlist.append(word[i])
    print(word)


    while True:
        while True:
            try:
                letter = str(input("Enter your letter: "))
                if not letter.isalpha() or not len(letter)==1:
                    raise Exception
            except:
                pass
            else:
                break
        print(hgstep[errornum])
        if letter in wordlist:
            for i in range(len(wordlist)):
                if wordlist[i]==letter:
                    guessedlist[i] = letter
            printlist(guessedlist)
            if letter in guessedlist:
                print("Already guessed this one!")
        else:
            if(errornum==6):
                print("You DIED!")
                break
            else:
                errornum+=1
                print("Incorrect, try again.")
                print(hgstep[errornum])
                printlist(guessedlist)
            
        if(wordlist==guessedlist):
            print("You did it!")
            break
"""