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
    print(secret_word)
# words=loadData()
# get_secret_word(words)