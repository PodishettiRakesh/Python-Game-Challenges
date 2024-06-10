import random
deck={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
def deck_creation(deck):
    cards=[]
    for key,value in deck.items():
        cards.append(key)
    random.shuffle(cards)
    return cards    
# print(deck_creation(deck))

def dealing_cards(cards):
    return cards.pop()


def Calculate_Score(Player_cards):
    score=0
    for card in Player_cards:
        score+=deck[card]
    if "A" in Player_cards and score>=21:
        score-=10
    return score

# print(Calculate_Score(["5","A"]))

def main():
    cards=deck_creation(deck)
    player1=[cards.pop(),cards.pop()]
    player2=[cards.pop(),cards.pop()]
    while True:
        # print(player1)
        player1_Score=Calculate_Score(player1)
        print(f"your cards: {player1} and score is: {player1_Score}")

        if player1_Score>=21:
            print("you loss the game!")
            return
        choice=input("enter Y to hit card or N to stand: ")
        choice=choice.lower()
        if choice=="y":
            player1.append(dealing_cards(cards))
        else:
            break

     
    while Calculate_Score(player2)<17:
        player2.append(dealing_cards(cards))

    player2_score=Calculate_Score(player2)
    print(f"dealer cards: {player2} and score is: {player2_score}")
    
    if player1_Score>player2_score:
        print("you are winner")
    if player2_score>player1_Score and player2_score<21:
        print("dealer is winner")

    if player2_score>=21:
        print("you are winner") 
main()
