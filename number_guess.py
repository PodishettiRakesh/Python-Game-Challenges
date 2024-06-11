import random
def generateNumber():
    num=random.randint(1,100)
    return num
# print(generateNumber())
def get_player_guess():
    guess=int(input("enter your number: "))
    return guess
# print(get_player_guess())