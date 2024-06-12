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

guessed=[]
def display(word):
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
        guessed.append(letter)
        return True
    return False
# print(guessed_letter("K","ramu"))
# print(guessed)
