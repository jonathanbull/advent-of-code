import copy

head_journey = []
tail_journey = []

class Rope(object):
    def __init__(self, start_x, start_y):
        self.head = Coordinate(start_x, start_y)
        self.tail = Coordinate(start_x, start_y)

    def tail_is_touching_head(self):
        return abs(self.head.x - self.tail.x) <= 1 and abs(self.head.y - self.tail.y) <= 1

    def move_head(self, direction, count):
        for _ in range(0, count):
            self.head.move(direction)

            if self.tail_is_touching_head() == False:
                # The tail is no longer touching the head
                if self.head.x == self.tail.x or self.head.y == self.tail.y:
                    # Tail is still in the same row/column as head (e.g. 2 across)
                    # Travel along one in the same direction
                    self.tail.move(direction)
                else:
                    # Tail is not in the same row/column as head (e.g. 1 across, 2 up)
                    # Travel to the previous position head was in, which will be a diagonal move
                    self.tail.x = head_journey[-1].x
                    self.tail.y = head_journey[-1].y

            head_journey.append(copy.copy(self.head))
            tail_journey.append(copy.copy(self.tail))

            print(self)

    def __str__(self):
        return 'Head: {} | Tail: {}.'.format(self.head, self.tail)


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

    def position_key(self):
        return 'x{}y{}'.format(self.x, self.y)

    def __str__(self):
        return '[{}, {}]'.format(self.x, self.y)


with open('input.txt') as input_file:
    rope = Rope(0, 0)

    for line in input_file:
        line = line.strip()
        direction = line[0]
        count = int(line[2:])
        print(line)
        rope.move_head(direction, count)

print()
print('-' * 50)
tail_visited = {c.position_key() for c in tail_journey}
print('Positions rope tail visited at least once: {}'.format(len(tail_visited)))
