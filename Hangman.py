def loadData():
    with open("Hangman_words.txt","r")as f:
        data=f.read()
    words=data.split("\n")
    words.pop()
    print(words)
loadData()