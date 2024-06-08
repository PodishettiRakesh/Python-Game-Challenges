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

user_score=0
computer_score=0

def determineWinner(user,computer):
    if user==computer:
        return "It's Tie"
    elif user=="rock":
        if computer=="paper":
            computer_score=computer_score+1
            return "computer won"
        else:
            user_score=user_score+1
            return "you won"
        
    
    elif user=="scissor":
        if computer=="rock":
            computer_score=computer_score+1
            return "computer won"
        else:
            user_score=user_score+1
            return "you won"

    elif user=="paper":
        if computer=="scissor":
            computer_score=computer_score+1
            return "computer won"
        else:
            user_score=user_score+1
            return "you won"
# user=getUserChoice()
# comp=getComputerChoice()
# print(determineWinner(user,comp))

def check_pattern(user_choices):

def play():
    print("welcome to the game")
    print("You can start the game by selecting 'rock', 'scissors' or 'paper'.")
    print("Choose continuously until you create a pattern.")
    print("Examples of patterns:")
    print("Rock, rock, rock, rock, etc.")
    print("Rock, scissors, rock, scissors, etc.")
    print("Rock, scissors, paper, rock, scissors, paper, etc.")
    print("Paper, paper, paper, paper, etc.")
    print("See that you will lose.")
    userPattern=[]
    
    while True:

        user=getUserChoice()
        comp=getComputerChoice()
        userPattern.append(user)
        print(f"you choose: {user}")
        print(f"computer choice: {comp}")
        print(determineWinner(user,comp))

        if check_pattern(user):
            print("You formed a pattern. You lose!")
            break

        play=input("y for play again: ")
        if play!="y":
            break
play()