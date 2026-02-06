import copy
from asset import Grid

class GridWorld:
    def __init__(self, size = 4):
        self.size = size
        self.grid = Grid(size, size)
    
    def iterative_policy_evaluation(self, steps = 1, discount = 1, reward = -1, threshold=1e-10):
        while steps > 0:
            delta = 0
            
            grid_copy = copy.deepcopy(self.grid.grid)
            new_grid = copy.deepcopy(self.grid.grid)
            
            for r in range(self.grid.rows):
                for c in range(self.grid.cols):
                    if (r, c) == (0, 0) or (r, c) == (3, 3):
                        continue
                    
                    v = 0
                    
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_r = r + dir[0]
                        new_c = c + dir[1]
                        if self.grid.is_out_of_bounds(new_r, new_c):
                            v += self.state_value(reward, discount, grid_copy, r, c)
                        else:
                            v += self.state_value(reward, discount, grid_copy, new_r, new_c)
                    
                    new_grid[r][c] = v
                    delta = max(delta, abs(v - grid_copy[r][c]))
                    
            self.grid.grid = new_grid
            if delta < threshold:
                break
            steps -= 1
            
        return self.grid.grid

    def state_value(self, reward, discount, grid, r, c):
        return 0.25 * (reward + discount * grid[r][c])
    
    def render(self, k):
        print("k =", k)
        self.grid.print_grid()
        print("/n")

if __name__ == "__main__":
    for k in [0, 1, 2, 3, 10, 1000]:
        policy = GridWorld(4)
        policy.iterative_policy_evaluation(steps = k)
        policy.render(k)