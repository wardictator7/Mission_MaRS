def read_obstacles(filename): #  Reading obstacle positions from obstacles.txt

    obstacles = []
    with open(filename, 'r') as f:
        for line in f:
            obstacles.append([int(x) for x in line.strip().split()])
    return obstacles

def create_arena(obstacles, size):

    # Initialize all positions to 1
    # If a point has obstacle it is marked as 0
    arena = [[1 for _ in range(size)] for _ in range(size)]

    # Center position (reference point)
    center = size // 2

    for obstacle in obstacles:
        n, e, s, w = obstacle

        # Calculate absolute position relative to center
        row = center - n + s  # North decreases row, South increases
        col = center - w + e  # West decreases column, East increases

        # Mark position if within bounds
        if 0 <= row < size and 0 <= col < size:
            arena[row][col] = 0

    return arena

def print_arena(arena): # Printing arena matrix

    for row in arena:
        print(' '.join(str(cell) for cell in row))
    print("\nKey: 0 = Obstacle, 1 = Safe Path")

f = read_obstacles("obstacles.txt")
a_size = 11
arena = create_arena(f, a_size)

print("Arena Map:")
print_arena(arena)