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