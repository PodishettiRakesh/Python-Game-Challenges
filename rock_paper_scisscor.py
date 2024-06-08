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
            user_score +=1
            return "you won"
        
    
    elif user=="scissor":
        if computer=="rock":
            computer_score +=1
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

def check_pattern(user_pattern):
    if len(user_pattern) < 3:
        return False

    # Check for the same choice repeated
    if all(choice == user_pattern[0] for choice in user_pattern):
        return True

    # Check for alternating choices (e.g., rock, scissors, rock, scissors, etc.)
    if len(user_pattern) % 2 == 0:
        half = len(user_pattern) // 2
        if user_pattern[:half] == user_pattern[half:]:
            return True

    # Check for cyclic pattern (e.g., rock, scissors, paper, rock, scissors, paper, etc.)
    pattern_length = len(set(user_pattern))
    if len(user_pattern) % pattern_length == 0:
        cycle = user_pattern[:pattern_length]
        for i in range(0, len(user_pattern), pattern_length):
            if user_pattern[i:i + pattern_length] != cycle:
                return False
        return True

    return False

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

        if check_pattern(userpattern):
            print("You formed a pattern. You lose!")
            break

        play=input("y for play again: ")
        if play!="y":
            break
play()