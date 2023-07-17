# Nested list (2D list) containing (',', '0') characters - forming grid-like structure
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# Outer for loop: Iterates through the columns of the grid
for col in range(len(grid[0])): # 'col' return number of columns in a grid (5)
    # Inner for loop: iterates through each row of the grid 
    for row in grid:           # assigns each row to the variable 'row' for each iteration
        print(row[col],end='') # prints element at the specific column('col') within each row - retrive character from current row and column and prints it
    print() # prints newline character after each column is printed


