import collections
import string

# Given a letter, get its elevation
def get_elevation(letter):
    if letter == 'S':
        # Current position (S) has elevation equivalent to 'a'
        return string.ascii_lowercase.index('a')
    elif letter == 'E':
        # End position (E) has elevation equivalent to 'z'
        return string.ascii_lowercase.index('z')

    return string.ascii_lowercase.index(letter)


def find_letter_in_grid(grid, letter):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == letter:
                return x, y

    return None

# Breadth first search, adapted from https://stackoverflow.com/a/47902476/526495
def find_shortest_path_in_grid(grid, start_letter, end_letter):
    start_x, start_y = find_letter_in_grid(grid, start_letter)
    width = len(grid[0])
    height = len(grid)
    start = (start_x, start_y)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        current_letter = grid[y][x]
        current_letter_elevation = get_elevation(current_letter)

        if current_letter == end_letter:
            # Found shortest path
            return path

        neighbours = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        for nx, ny in neighbours:
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                # Cell is out of bounds
                continue

            if (nx, ny) in seen:
                # We've visited this cell already
                continue

            new_letter = grid[ny][nx]
            new_letter_elevation = get_elevation(new_letter)
            step_size = new_letter_elevation - current_letter_elevation

            if step_size > 1:
                # Step is too high
                continue

            queue.append(path + [(nx, ny)])
            seen.add((nx, ny))


def get_grid():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            grid.append([*line.strip()])

    return grid


def print_grid(grid):
    for _, row in enumerate(grid):
        for _, value in enumerate(row):
            print(value, end='')
        print()


grid = get_grid()
print_grid(grid)
print()

shortest_path = find_shortest_path_in_grid(grid, 'S', 'E')

if shortest_path:
    step_count = len(shortest_path) - 1 # Starting step doesn't count
    print('Shortest path ({}): '.format(step_count), end='')
    for x, y in shortest_path:
        print('{}'.format(grid[y][x]), end='')
else:
    print('No path possible.')
