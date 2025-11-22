#                   ----- Project Cell Learner -----

import math

# --- Beállítások ---
width, height = 20, 20

start = (0, 0)
goal = (15, 10)
reset_cells = {(5, 5), (8, 3), (7, 7), (1, 0)}  # ide lépve visszadob

# --- Értéktérkép létrehozása ---
grid = [[0 for _ in range(width)] for _ in range(height)]

for y in range(height):
    for x in range(width):
        dist = math.hypot(goal[0] - x, goal[1] - y)
        grid[y][x] = 1 / (dist + 1)

# --- Szimuláció ---
pos = start
path = [pos]

for tick in range(300):  # max 300 lépés
    x, y = pos

    # Szomszédok
    neighbors = []
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((grid[ny][nx], (nx, ny)))

    if not neighbors:
        break

    # Legnagyobb értékű szomszéd
    neighbors.sort(reverse=True, key=lambda v: v[0])
    next_pos = neighbors[0][1]

    # Lépés
    pos = next_pos
    path.append(pos)

    # Ha cél
    if pos == goal:
        print("Goal reached")
        break

    # Ha reset cella
    if pos in reset_cells:
        print(f"Stepped on reset cell: {pos}, back to start")
        # Csak most állítjuk 0-ra
        grid[pos[1]][pos[0]] = 0
        pos = start
        path.append(pos)

print("Way:", path)
