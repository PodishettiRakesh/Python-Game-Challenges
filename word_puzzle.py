import random
def grid(row,col):
    board=[]
    letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']
    for _ in range(row):
        row=[]
        for _ in range(col):
            row.append(random.choice(letter))
        board.append(row)
    print(board)
    return board
# grid(6,6)


def readfile(filename):
    with open(filename,"r") as file:
        data=file.read()
        words=data.split("\n")    
    return words
# print(readfile("words_puzzle.txt"))

# def checking_horizontal(board, valid_word):
    # for i in range(len(board)):
    #     s=""
    #     for j in range(len(board[0])):
    #         s+=board[i][j]
    #     if valid_word in s:
    #         return True
    # return False

def check_horizontal(matrix, valid_words):
    lis=[]
    for word in valid_words:
        word_len=len(word)
        for i in range(len(matrix)):
            new_word=""
            for j in range(len(matrix[0])):
                new_word+=matrix[i][j]
            if word in new_word:
                print("word found")
                startIndex=new_word.index(word)
                lis.append((word,(i,startIndex),(i,startIndex+(word_len-1))))
            rev_word=word[::-1]
            if rev_word in new_word:
                print("word found")
                startIndex=new_word.index(rev_word)
                lis.append((word,(i,startIndex+(word_len-1),(i,startIndex))))
    return lis


# matrix=grid(5,6)
# print(matrix)
# print(check_horizontal(matrix,["cy","ad","xf","cd","amg","mg"]))
def check_vertical(matrix, valid_words):
    found_words = []
    num_cols = len(matrix[0])
    for word in valid_words:
        word_len = len(word)
        for col in range(num_cols):
            col_str = ''.join([matrix[row][col] for row in range(len(matrix))])
            if word in col_str:
                start_index = col_str.index(word)
                found_words.append((word, (start_index, col), (start_index + word_len - 1, col)))
            reversed_word = word[::-1]
            if reversed_word in col_str:
                start_index = col_str.index(reversed_word)
                found_words.append((word, (start_index + word_len - 1, col), (start_index, col)))
    return found_words        

board=grid(6,7)
for i in board:
    print(i)
print(check_vertical(board,["cy","xc","hb","df"]))



def check_diagonal_tl_br(matrix, valid_words):
    found_words = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for word in valid_words:
        word_len = len(word)
        # Check top-left to bottom-right diagonals
        for row in range(num_rows):
            for col in range(num_cols):
                if row + word_len <= num_rows and col + word_len <= num_cols:
                    diag_str = ''.join([matrix[row + k][col + k] for k in range(word_len)])
                    if word == diag_str:
                        found_words.append((word, (row, col), (row + word_len - 1, col + word_len - 1)))
                    if word[::-1] == diag_str:
                        found_words.append((word, (row + word_len - 1, col + word_len - 1), (row, col)))
    return found_words
