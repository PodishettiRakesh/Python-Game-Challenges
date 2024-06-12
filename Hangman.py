import random
def loadData():
    with open("Hangman_words.txt","r")as f:
        data=f.read()
    words=data.split("\n")
    words.pop()
    return words
# loadData()

def get_secret_word(words):
    secret_word=random.choice(words)
    return secret_word
# words=loadData()
# get_secret_word(words)

# guessed=[]
def display(word,guessed):
    for i in word:
        if i in guessed:
            print(i,end=" ")
        else:
            print("_",end=" ")
# words=loadData()
# word=get_secret_word(words)
# display(word)

def guessed_letter(letter,secretWord):
    if letter in secretWord:
        return True
    return False
def checkwin(guessed,word):
    guess=""
    for each in guessed:
        guess+=each
    if guess==word:
        return True
def play():
    print("welcome to the Hangaman game")
    data=loadData()
    word=get_secret_word(data)
    print(word)
    print(f"i am thinking of a word is {len(word)} letters long")
    chance=8
    guessed=[]
    letters="abcdefghijklmnopqrstuvwxyz"
    print(guessed)
    while chance>0:
        if checkwin(guessed,word):
            print("you revealed the won! congratulations")
        
        print(f"you have {chance} chancess left")
        display(word,guessed)
    
        while True:
            try:
                letter = input("Please guess a letter: ").strip().lower()
                if letter not in letters or len(letter) != 1:
                    print("Invalid input. Please enter a single letter.")
                elif letter in guessed:
                    print("You already guessed that letter.")
                else:
                    break
            except ValueError:
                print("Invalid input.")
        
        if guessed_letter(letter,word):
            guessed.append(letter)
            print(f"good guess {display(word,guessed)}")
            chance-=1
        else:
            chance-=1
            print("oops! you guessed wrong letter")
    print("you loss the game")

play()
        
