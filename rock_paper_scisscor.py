import random
def getUserChoice():
    while True:
        try:
            userChoice=input("enter your choice: ")
            userChoice=userChoice.lower()
            print(userChoice)
            if userChoice in ["rock","paper","scissor"]:
                break
            else:
                print("please enter valids option")
        except ValueError:
            print("please enter valid choice")

    return userChoice
# print(getUserChoice())

def getComputerChoice():
    options=["rock","paper","scissor"]
    choice=random.choice(options)
    return choice
# print(getComputerChoice())

def determineWinner(user,computer):
    if user==computer:
        return "It's Tie"
    elif user=="rock":
        if computer=="paper":
            return "computer won"
        else:
            return "you won"
    
    elif user=="scissor":
        if computer=="rock":
            return "computer won"
        else:
            return "you won"

    elif user=="paper":
        if computer=="scissor":
            return "computer won"
        else:
            return "you won"
# user=getUserChoice()
# comp=getComputerChoice()
# print(determineWinner(user,comp))

def play():
    print("welcome to the game")
    
    while True:
        user=getUserChoice()
        comp=getComputerChoice()
        print(determineWinner(user,comp))

        play=input("y for play again: ")
        if play!="y":
            break
play()