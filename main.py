import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import matplotlib

matplotlib.use("TkAgg")

# Grid configuration
GRID_SIZE = 50
PROB_INFECT = 0.3 
RECOVERY_TIME = 10

# Cell states
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

def initialize_grid(size, initial_infected=1):
    grid = np.zeros((size, size), dtype=int)
    for _ in range(initial_infected):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        grid[x, y] = INFECTED
    return grid

def update_grid(grid, recovery_times):
    new_grid = np.copy(grid)
    size = grid.shape[0]
    for i in range(size):
        for j in range(size):
            if grid[i, j] == SUSCEPTIBLE:
                neighbors = [grid[x, y] for x, y in get_neighbors(i, j, size)]
                if INFECTED in neighbors and random.random() < PROB_INFECT:
                    new_grid[i, j] = INFECTED
                    recovery_times[i, j] = RECOVERY_TIME
            elif grid[i, j] == INFECTED:
                recovery_times[i, j] -= 1
                if recovery_times[i, j] <= 0:
                    new_grid[i, j] = RECOVERED
    return new_grid

def get_neighbors(x, y, size):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            neighbors.append((nx, ny))
    return neighbors

def simulate(steps=50):
    grid = initialize_grid(GRID_SIZE)
    recovery_times = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    cmap = mcolors.ListedColormap(['white', 'red', 'green'])
    plt.figure(figsize=(6, 6))
    for step in range(steps):
        plt.clf()
        plt.imshow(grid, cmap=cmap, origin='upper')
        plt.title(f"Step {step}")
        plt.pause(0.1)
        grid = update_grid(grid, recovery_times)
    plt.show()

if __name__ == "__main__":
    simulate()
