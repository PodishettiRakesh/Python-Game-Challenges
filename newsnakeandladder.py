

import random
def initialize_game():
    board=[]
    sum=100
    for i in range(10):
        r=[]
        for j in range(10):
            r.append(sum)
            sum-=1
        board.append(r)
    board[9]=board[9][::-1]
    snakes={99:3,82:45,65:50,49:32,30:16,15:6}
    ladders={5:13,18:34,32:44,52:74,70:93}
    for i in range(10):
        for j in range(10):
            if board[i][j] in snakes.keys():
                board[i][j]="SH"
            if board[i][j] in ladders.keys():
                board[i][j]="LB"
            if board[i][j] in snakes.values():
                board[i][j]="ST"
            if board[i][j] in ladders.values():
                board[i][j]="LT"
    return board,snakes,ladders

def display(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print('%-4s' %board[i][j],end=" ")
        print()

def register_player():
    name=input("Enter Players Name: ")
    position=0
    return name,position

def roll_die():
    input("press enter to roll the dice ")
    dice=random.randint(1,6)
    print("The value is: ",dice)
    return dice

def move_player(board,snakes,ladders,player,dice):
    position=player+dice
    if position<=100:
        print("Player Position ",position)
        if position in snakes.keys():
            player=snakes[position]
            print("There is a snake here. Go to: ",snakes[position])
        elif position in ladders.keys():
            player=ladders[position]
            print("There is a ladder here. Go to: ",ladders[position])
        else:
            player= position
    
    return player
def check_win(position):
    if position==100:
        return True
    else:
        return False
    
def display_positions(players):
    for i in range(len(players)):
        print("player: ",players[i][0],"at position: ",players[i][1])


def playgame():
    print("welcome to Snakes and Ladders Game")
    board,snakes,ladders=initialize_game()
    display(board)
    while True:
        no_of_players=int(input("how many players are playing: "))
        details=[]
        if no_of_players<=0:
            print("Atleast one player should be played")
        else:
            break
    for i in range(no_of_players):
        name,position=register_player()
        details.append([name,position])
    while True:
        for i in range(no_of_players):
            display_positions(details)
            print("Player ", details[i][0], "'s turn")
            dice = roll_die()
            position = details[i][1]
            position = move_player(board, snakes, ladders, position, dice)
            details[i][1] = position
            if check_win(details[i][1]):
                print("Player ", details[i][0], "won the game")
                return


playgame()

