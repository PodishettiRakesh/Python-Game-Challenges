import random
deck={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
def deck_creation(deck):
    cards=[]
    for key,value in deck.items():
        cards.append(value)
    random.shuffle(cards)
    return cards    
# print(deck_creation(deck))

def dealing_cards(cards):
    return cards.pop()

