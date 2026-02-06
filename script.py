grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLS = len(grid[0])
ROWS = len(grid)

def iterPolicyEval(
    policy,
    threshold=1e-10,
) :
    delta = 0
    while delta >= threshold:
        for r in range(ROWS):
            for c in range(COLS):
                v = grid[r][c]
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dir in dirs:
                    new_r = r + dir[0]
                    new_c = c + dir[1]
                    grid[r][c] += 1/4 * (-1 + 1* grid[new_r][new_c])
                delta = max(delta, abs(v - grid[r][c]))
    return grid

policy = None  # Placeholder for policy, not used in this example
result = iterPolicyEval(policy)
            