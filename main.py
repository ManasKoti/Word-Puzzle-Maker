import random

ALPHABETS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
             "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"]

def create_grid(dimension):
    grid = []
    for _ in range(dimension):
        row = []
        for _ in range(dimension):
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
    return grid

def accept_word():
    word = input("Enter the word to be inserted: ")
    position = input("Enter the position (x, y, direction): ").split()
    position = (int(position[0]), int(position[1]), position[2])
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