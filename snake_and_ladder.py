# import random
# def generate_board():
#     board=[]
#     for _ in range(0,10):
#         row=[]
#         for _ in range(0,10):
#             row.append(0)
#         board.append(row)
#     return board
# def displayBoard(board,player_position):
#     for i in range(len(board)):
#         row=''
#         for j in range(len(board[i])):
#             if i * 10 + j == player_position:
#                 row+='P '
#             else:
#                 row+=str(board[i][j])+' '
#         print(row)
# def rollDice():
#     return random.randint(1,6)
# def move_player(player_position,dice_roll):
#     new_postion=player_position+dice_roll
#     if new_postion>99:
#         new_postion=99
#     return new_postion
# def checkWin(player_position):
#     return  player_position==99
# def checkSnakesAndLadder(player_position,snakes,ladders):
#     if player_position in snakes:
#         print('landed in snake, now going to snake tail')
#         return snakes[player_position]
#     elif player_position in ladders:
#         print('landed on ladder. climbing to the top end of the ladder')
#         return ladders[player_position]
#     return player_position
# def playSnakeAndLadderGame():
#     board=generate_board()
#     player_position=0
#     snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
#     ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
#     print('Welcome to snake and ladder game')
#     while True:
#         displayBoard(board,player_position)

#         input('press enter to load the dice')

#         dice_roll=rollDice()
#         print(dice_roll)
#         player_position=move_player(player_position,dice_roll)
#         player_position=checkSnakesAndLadder(player_position,snakes,ladders)

#         if checkWin(player_position):
#             print('Congratulations You won the game')
#             break
# playSnakeAndLadderGame()
import random
def generate_board():
    board=[]
    for i in range(10):
        row=[0]*10
        print(row)
        board.append(row)
    number=99
    for i in range(10):
        for j in range(10):
            board[i][j]=number
            number-=1
    return board
# print(generate_board())

def displayBoard(board,player_position):
    for i in range(len(board)):
        row=''
        for j in range(len(board[i])):
            if i*10+j==player_position:
                row+='P '
            else:
                row+=str(board[i][j])+' '
        print(row)
        
def rollDice():
    return random.randint(1,6)
def move_player(player_position,dice_roll):
    new_postion=player_position+dice_roll
    if new_postion>99:
        new_postion=99
    return new_postion
def checkWin(player_position):
    return  player_position==99
def checkSnakesAndLadder(player_position,snakes,ladders):
    if player_position in snakes:
        print('landed in snake, now going to snake tail')
        return snakes[player_position]
    elif player_position in ladders:
        print('landed on ladder. climbing to the top end of the ladder')
        return ladders[player_position]
    return player_position
def playSnakeAndLadderGame():
    board=generate_board()
    player_position=0
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    print('Welcome to snake and ladder game')
    while True:
        displayBoard(board,player_position)
        input('press enter to load the dice')
        dice_roll=rollDice()
        print(dice_roll)
        player_position=move_player(player_position,dice_roll)
        player_position=checkSnakesAndLadder(player_position,snakes,ladders)
        if checkWin(player_position):
            print('Congratulations You won the game')
            break
# playSnakeAndLadderGame()
