import random

# Step 1: Define the Matrix and Valid Words
def create_matrix(row, col):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return [[random.choice(letters) for _ in range(col)] for _ in range(row)]

def read_valid_words(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words

# Step 2: Create a Function to Check Horizontal Words
def check_horizontal(matrix, valid_words):
    found_words = []
    for word in valid_words:
        word_len = len(word)
        for i in range(len(matrix)):
            row_str = ''.join(matrix[i])
            if word in row_str:
                start_index = row_str.index(word)
                found_words.append((word, (i, start_index), (i, start_index + word_len - 1)))
            reversed_word = word[::-1]
            if reversed_word in row_str:
                start_index = row_str.index(reversed_word)
                found_words.append((word, (i, start_index + word_len - 1), (i, start_index)))
    return found_words

# Step 3: Create a Function to Check Vertical Words
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

# Step 4: Create a Function to Check Diagonal Words (Top-Left to Bottom-Right)
def check_diagonal_tl_br(matrix, valid_words):
    found_words = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for word in valid_words:
        word_len = len(word)
        for row in range(num_rows):
            for col in range(num_cols):
                if row + word_len <= num_rows and col + word_len <= num_cols:
                    diag_str = ''.join([matrix[row + k][col + k] for k in range(word_len)])
                    if word == diag_str:
                        found_words.append((word, (row, col), (row + word_len - 1, col + word_len - 1)))
                    if word[::-1] == diag_str:
                        found_words.append((word, (row + word_len - 1, col + word_len - 1), (row, col)))
    return found_words

# Step 5: Create a Function to Check Diagonal Words (Top-Right to Bottom-Left)
def check_diagonal_tr_bl(matrix, valid_words):
    found_words = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for word in valid_words:
        word_len = len(word)
        for row in range(num_rows):
            for col in range(num_cols):
                if row + word_len <= num_rows and col - word_len >= -1:
                    diag_str = ''.join([matrix[row + k][col - k] for k in range(word_len)])
                    if word == diag_str:
                        found_words.append((word, (row, col), (row + word_len - 1, col - word_len + 1)))
                    if word[::-1] == diag_str:
                        found_words.append((word, (row + word_len - 1, col - word_len + 1), (row, col)))
    return found_words

# # Step 6: Create a Function to Validate Words in a Given Sequence
# def validate_words(sequence, valid_words):
#     found_words = []
#     for word in valid_words:
#         if word in sequence:
#             found_words.append(word)
#         elif word[::-1] in sequence:
#             found_words.append(word)
#     return found_words

# Step 7: Integrate All Functions to Search the Entire Matrix
def search_words(matrix, valid_words):
    found_words = []
    found_words.extend(check_horizontal(matrix, valid_words))
    found_words.extend(check_vertical(matrix, valid_words))
    found_words.extend(check_diagonal_tl_br(matrix, valid_words))
    found_words.extend(check_diagonal_tr_bl(matrix, valid_words))
    return found_words

# Step 8: Display the Results
def display_results(found_words):
    print("Found Words:")
    for word, start, end in found_words:
        print(f"- {word} ({start} to {end})")

# Example Usage
if __name__ == "__main__":
    matrix = [
        ['t', 'h', 'i', 's'],
        ['w', 'a', 't', 's'],
        ['o', 'a', 'h', 'g'],
        ['f', 'g', 'd', 't']
    ]
    valid_words = ['this', 'what', 'dog', 'cat']

    # Display the matrix
    for row in matrix:
        print(' '.join(row))
    
    # Search for valid words
    found_words = search_words(matrix, valid_words)

    # Display the results
    display_results(found_words)
