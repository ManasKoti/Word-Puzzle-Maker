import random

ALPHABETS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def create_grid(dimension):
    grid = []
    for i in range(dimension):
        row = []
        for i in range(dimension):
            random_letter = random.choice(ALPHABETS)
            row.append(random_letter)
        grid.append(row)
    return grid

def insert_word(grid, word, position):
    x, y, direction = position             #x = row, y = column
    word = word.upper()
    if direction == 'across':
        for i in range(len(word)):
            grid[x][y + i] = word[i]
    elif direction == 'down':
        for i in range(len(word)):
            grid[x + i][y] = word[i]
    elif direction == 'diagonal_d':
        for i in range(len(word)):
            grid[x + i][y + i] = word[i]
    elif direction == 'diagonal_u':
        for i in range(len(word)):
            grid[x - i][y + i] = word[i]
    return grid

def accept_word():
    word = input("Enter the word to be inserted: ")
    x = (int(input("Enter the row number: "))-1)
    y = (int(input("Enter the column number: "))-1)
    direction = input("Enter the direction (across/down/diagonal_u(right)/diagonal_d(right)): ")
    position = (x, y, direction)
    return word, position

dimension = int(input("Enter the dimension of the grid: "))
grid = create_grid(dimension)
word, position = accept_word()
grid = insert_word(grid, word, position)
keep_inserting = True
while keep_inserting:
    insert_more = input("Do you want to insert more words? (yes/no): ")
    if insert_more.lower() == 'yes':
        word, position = accept_word()
        grid = insert_word(grid, word, position)
    else:
        keep_inserting = False
    
for row in grid:
    print(' '.join(row))