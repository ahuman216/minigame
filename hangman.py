def hangman():
    
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
