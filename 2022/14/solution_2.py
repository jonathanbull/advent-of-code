import os

class Cave(object):
    def __init__(self, rock_positions, sand_start_x, sand_start_y):
        max_x = max(rock_positions, key=lambda r:r[0])[0]
        max_y = max(rock_positions, key=lambda r:r[1])[1]

        # Add two rows to represent the floor
        max_y += 2
        self.floor_index = max_y

        cells = []
        for y in range(0, max_y + 1):
            row = {}
            for x in range(0, max_x + 1):
                if x == sand_start_x and y == sand_start_y:
                    row[x] = '+'
                elif (x, y) in rock_positions:
                    row[x] = '#'
                elif y == max_y:
                    # Floor
                    row[x] = '#'
                else:
                    row[x] = '.'
            cells.append(row)

        self.rock_positions = rock_positions
        self.cells = cells

        self.sand_start_x = sand_start_x
        self.sand_start_y = sand_start_y

    def add_col_left(self):
        new_col_index = list(self.cells[0]) - 1
        for y, row in enumerate(self.cells):
            if y == self.floor_index:
                # Extend the floor
                row[new_col_index] = '#'
            else:
                # Air
                row[new_col_index] = '.'

    def add_col_right(self):
        new_col_index = self.get_width()
        for y, row in enumerate(self.cells):
            if y == self.floor_index:
                # Extend the floor
                row[new_col_index] = '#'
            else:
                # Air
                row[new_col_index] = '.'

    def get_width(self):
        return len(self.cells[0])

    def get_height(self):
        return len(self.cells)

    def drop_grain_of_sand(self):
        current_x, current_y = self.sand_start_x, self.sand_start_y

        if cave.cells[current_y][current_x] == 'o':
            # We're full up
            return None

        cave.cells[current_y][current_x] = 'o'

        # Every iteration moves the sand one pixel
        while True:
            southerly_positions = get_southerly_positions(current_x, current_y)
            for i, position in enumerate(southerly_positions):
                target_x, target_y = position[0], position[1]

                if target_x == 0:
                    cave.add_col_left()
                elif target_x == cave.get_width():
                    cave.add_col_right()

                if cave.cells[target_y][target_x] == '.':
                    # Target cells is free, move the sand
                    cave.cells[target_y][target_x] = 'o'

                    # Restore original value
                    if current_x == self.sand_start_x and current_y == self.sand_start_y:
                        cave.cells[current_y][current_x] = '+'
                    else:
                        cave.cells[current_y][current_x] = '.'

                    current_x, current_y = target_x, target_y

                    # We're finished with this move
                    # print_cave(self)
                    break

                if i == len(southerly_positions) - 1:
                    # All positions exhausted, settle
                    return (target_x, target_y)


def print_cave(cave):
    # Clear the terminal
    os.system('clear')

    # We trim the left of the cave if it doesn't contain anything other than air
    # Ignoring the floor, find the first column with anything of note
    min_x = cave.get_width()
    for y, row in enumerate(cave.cells):
        if y == cave.get_height() - 1:
            break
        for x, cell in row.items():
            if x >= min_x:
                break
            if cell != '.':
                min_x = x

    for _, row in enumerate(cave.cells):
        for x, _ in enumerate(row):
            if x < min_x:
                continue
            print(row[x], end='')
        print()
    print()


# Given an xy coordinate, get it's southerly positions in the order we should
# traverse them (south, southwest, southeast)
def get_southerly_positions(x, y):
    # The top row of the cave has a y value of 0
    return [
        (x, y + 1), # South
        (x - 1, y + 1), # Southwest
        (x + 1, y + 1), # Southeast
    ]


# Creates rocks between two vertical/horizontal points on a cave, inclusive of
# start and end
def create_rocks_between(start_x, start_y, end_x, end_y):
    rocks = []
    x_range = range(start_x, end_x+1) if start_x < end_x else range (end_x, start_x+1)
    y_range = range(start_y, end_y+1) if start_y < end_y else range (end_y, start_y+1)

    for x in x_range:
        for y in y_range:
            rock = (x, y)
            rocks.append(rock)

    return rocks


def get_rock_positions():
    rocks = []
    with open('input.txt') as input_file:
        for line in input_file:
            line = line.strip()
            coords = line.split(' -> ')
            for i, v in enumerate(coords):
                if i == 0:
                    continue
                last_x, last_y = coords[i-1].split(',')
                current_x, current_y = v.split(',')
                rocks.extend(create_rocks_between(int(last_x), int(last_y), int(current_x), int(current_y)))

    # Return, with duplicates stripped
    return set(rocks)


def create_cave():
    rock_positions = get_rock_positions()
    return Cave(rock_positions, 500, 0)


cave = create_cave()
# print_cave(cave)

sand_flowing = True
grains_dropped = 0
while True:
    settled_at = cave.drop_grain_of_sand()

    if settled_at != None:
        grains_dropped += 1
        print('{} grain(s) dropped.'.format(grains_dropped))
    else:
        # Into the abyss
        break

print('-' * 50)
print('Finished. {} grain(s) of sand came to rest before the source of the sand became blocked.'.format(grains_dropped))
