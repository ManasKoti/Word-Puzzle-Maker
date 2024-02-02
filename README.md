# Word Search Puzzle Maker

This Python script allows you to generate a random word search puzzle and insert words of your choice into the grid.

## How to Use

1. **Run the script:** Save the script as `main.py` and run it from the command line using `python main.py`.
2. **Enter grid dimension:** You will be prompted to enter the desired dimension of the grid (number of rows and columns).
3. **Insert words:** The script will create a random grid and then prompt you to insert words.
    * Enter the word you want to insert.
    * Enter the position of the word in the grid:
        * X coordinate (row number)
        * Y coordinate (column number)
        * Direction ("across" or "down")
    * You can insert multiple words by entering "yes" when asked if you want to insert more words.
4. **View the puzzle:** After finishing, the script will print the final grid with the inserted words.

## Example

Here is an example of how the script might work:

```
Enter the dimension of the grid: 5
Enter the word to be inserted: hat
Enter the position (x, y, direction): 1 0 down
Do you want to insert more words? (yes/no): no
Z R S D N
H G P Z P
A J K Y G
T G P Y H
Y W L K X
```

## Notes

* The script uses random letters to generate the grid.
* Words are inserted in uppercase letters.
* Words cannot be inserted diagonally or overlap with existing letters (This feature is planned for future).
* The script does not check if the inserted word is a valid word (This feature is planned for future).

### I hope this helps!
