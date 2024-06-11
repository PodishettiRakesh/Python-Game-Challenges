import random
def generateNumber():
    num=random.randint(1,100)
    return num
# print(generateNumber())
def get_player_guess():
    guess=int(input("enter your number: "))
    return guess
# print(get_player_guess())

def feedback(num,guess):
    
    if num>guess:
        return "too low"
    elif num<guess:
        return "too high"
    else:
        return "guessed"
def checkwin(num,guess):
    if num==guess:
        return True
    
def main():
    num=generateNumber()
    while True:
        guess=get_player_guess()
        print(feedback(num,guess))
        if checkwin(num,guess):
            return "you guessed correct and won the game"
main()
    
    