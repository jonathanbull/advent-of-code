import copy

head_journey = []
tail_journey = []

class Rope(object):
    def __init__(self, start_x, start_y, number_of_knots):
        self.knots = []
        for _ in range(number_of_knots):
            self.knots.append(Coordinate(start_x, start_y))

    def move_head(self, direction, count):
        head_knot = self.knots[0]
        tail_knot = self.knots[-1]

        for _ in range(0, count):
            head_knot.move(direction)
            for i, knot in enumerate(self.knots):
                if i > 0:
                    knot.move_to_adjacent_coordinate(self.knots[i-1].x, self.knots[i-1].y)
                    self.knots[i] = knot
            print(rope)
            print()

            head_journey.append(copy.copy(head_knot))
            tail_journey.append(copy.copy(tail_knot))

    def __str__(self):
        output = ''
        for i, knot in enumerate(self.knots):
            output += str(knot)
            if i == 0:
                output += ' <-- knot 0 (head)\n'
            elif i == len(self.knots) - 1:
                output += ' <-- knot ' + str(i) + ' (tail)'
            else:
                output += ' <-- knot ' + str(i) + '\n'

        return output


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'U':
            self.move_north()
        elif direction == 'R':
            self.move_east()
        elif direction == 'D':
            self.move_south()
        elif direction == 'L':
            self.move_west()

    def move_north(self):
        self.y += 1

    def move_east(self):
        self.x += 1

    def move_south(self):
        self.y -= 1

    def move_west(self):
        self.x -= 1

    def move_to_adjacent_coordinate(self, target_x, target_y):
        if abs(self.x - target_x) <= 1 and abs(self.y - target_y) <= 1:
            # Already touching
            return

        if self.x == target_x:
            # Same column
            self.y = (target_y - 1) if self.y < target_y else target_y + 1
        elif self.y == target_y:
            # Same row
            self.x = (target_x - 1) if self.x < target_x else target_x + 1
        else:
            # On a diagonal
            self.x = self.x + 1 if self.x < target_x else self.x - 1
            self.y = self.y + 1 if self.y < target_y else self.y - 1

    def position_key(self):
        return 'x{}y{}'.format(self.x, self.y)

    def __str__(self):
        return '[{}, {}]'.format(self.x, self.y)


with open('input.txt') as input_file:
    rope = Rope(0, 0, 10)

    for line in input_file:
        line = line.strip()
        direction = line[0]
        count = int(line[2:])
        print('== {} =='.format(line))
        rope.move_head(direction, count)

print()
print('-' * 50)
tail_visited = {c.position_key() for c in tail_journey}
print('Positions rope tail visited at least once: {}'.format(len(tail_visited)))
