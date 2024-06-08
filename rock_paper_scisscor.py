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
    global user_score, computer_score
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
    # global user_score, computer_score
    print("Welcome to the game!")
    print("You can start the game by selecting 'rock', 'scissors' or 'paper'.")
    print("Choose continuously until you create a pattern.")
    print("Examples of patterns:")
    print("Rock, rock, rock, rock, etc.")
    print("Rock, scissors, rock, scissors, etc.")
    print("Rock, scissors, paper, rock, scissors, paper, etc.")
    print("Paper, paper, paper, paper, etc.")
    print("See that you will lose.")
    user_pattern = []
    
    while True:
        user =getUserChoice()
        comp = getComputerChoice()
        user_pattern.append(user)
        print(f"You chose: {user}")
        print(f"Computer chose: {comp}")
        print(determineWinner(user, comp))
        print(f"User score: {user_score}, Computer score: {computer_score}")

        if check_pattern(user_pattern):
            print("You formed a pattern. You lose!")
            break

        play_again = input("Play again? (y for yes, any other key to stop): ")
        if play_again.lower() != 'y':
            break

    print(f"Final score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer won the game! Better luck next time.")
    else:
        print("It's a tie game!")

play()