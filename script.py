import copy
def print_grid(grid_data):
    """
    Prints a 2D list (list of lists) as a grid in the console.

    Args:
        grid_data (list of lists): The data to print in the grid.
    """
    # Determine the maximum width needed for each column
    widths = [max(len(str(item)) for item in col) for col in zip(*grid_data)]

    # Print the top border
    row_separator = f'+{"".join("-" * (width + 2) + "+" for width in widths)}'
    print(row_separator)

    for row in grid_data:
        # Print the row content
        row_str = '|'
        for i, item in enumerate(row):
            # Use f-strings for aligned formatting
            row_str += f' {str(item).ljust(widths[i])} |'
        print(row_str)
        # Print the separator after each row
        print(row_separator)

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLS = len(grid[0])
ROWS = len(grid)

def outOfBounds(r, c):
    return r < 0 or r >= ROWS or c < 0 or c >= COLS

def iterPolicyEval(
    grid,
    policy,
    threshold=1e-10,
    iter = 10
) :
    k = 1
    while True:
        delta = 0
        grid_copy = copy.deepcopy(grid)
        new_grid = copy.deepcopy(grid)
        print("k: ", k)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) == (0, 0) or (r, c) == (3, 3):
                    continue
                
                v = grid[r][c]
                
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r = r + dir[0]
                    new_c = c + dir[1]
                    if outOfBounds(new_r, new_c):
                        v += 0.25 * (-1 + 1 * grid_copy[r][c])
                    else:
                        v += 0.25 * (-1 + 1 * grid_copy[new_r][new_c])
                
                new_grid[r][c] = v
                delta = max(delta, abs(v - grid[r][c]))
                
        grid = new_grid
        print_grid(grid)
        print("\n")
        if delta < threshold or k == iter:
            break
        k += 1
        
    return grid

policy = None
result = iterPolicyEval(grid,policy)
print_grid(result)
            