def largest_cross(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    
    left = [[0] * cols for _ in range(rows)]
    right = [[0] * cols for _ in range(rows)]
    top = [[0] * cols for _ in range(rows)]
    bottom = [[0] * cols for _ in range(rows)]
    
    # Calcular left y top
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
                top[i][j] = 1 if i == 0 else top[i - 1][j] + 1
    
    # Calcular right y bottom
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = 1 if j == cols - 1 else right[i][j + 1] + 1
                bottom[i][j] = 1 if i == rows - 1 else bottom[i + 1][j] + 1
    
    max_size = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                max_size = max(max_size, size)
    
    return max_size

# Ejemplo de uso:
grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0]
]

print(largest_cross(grid))
