import os
import re

class Cave(object):
    def __init__(self, sensor_positions, beacon_positions):
        self.sensor_positions = sensor_positions
        self.beacon_positions = beacon_positions

    def get_all_positions(self):
        return self.sensor_positions + self.beacon_positions

    # Get all sensors, along with a third index that states the manhattan
    # distance from it's beacon
    # Example output:
    # [
    #     (0, 4, 10) <- x=0, y=4, manhattan_distance=10
    #     (4, 9, 3)  <- x=4, y=9, manhattan_distance=3
    # ]
    def get_sensor_positions_with_radius(self):
        results = []
        for i, sensor in enumerate(self.sensor_positions):
            beacon = self.beacon_positions[i]
            manhattan_distance = get_manhattan_distance(sensor, beacon)
            results.append((sensor[0], sensor[1], manhattan_distance))

        return results

    def is_coord_in_any_sensor_radius(self, coord):
        sensor_positions_with_radius = self.get_sensor_positions_with_radius()
        for sensor in sensor_positions_with_radius:
            if is_coord_in_sensor_radius(coord, (sensor[0], sensor[1]), sensor[2]):
                return True

        return False

    def get_min_x(self):
        return min(self.get_all_positions(), key=lambda r:r[0])[0]

    def get_min_x_including_sensor_radiuses(self):
        position_min_x = self.get_min_x()
        position_with_radius_min = min(self.get_sensor_positions_with_radius(), key=lambda r:r[0]-r[2])
        position_with_radius_min_x = position_with_radius_min[0] - position_with_radius_min[2]
        return min(position_min_x, position_with_radius_min_x)

    def get_max_x(self):
        return max(self.get_all_positions(), key=lambda r:r[0])[0]

    def get_max_x_including_sensor_radiuses(self):
        position_max_x = self.get_max_x()
        position_with_radius_max = max(self.get_sensor_positions_with_radius(), key=lambda r:r[0]+r[2])
        position_with_radius_max_x = position_with_radius_max[0] + position_with_radius_max[2]
        return max(position_max_x, position_with_radius_max_x)

    def get_min_y(self):
        return min(self.get_all_positions(), key=lambda r:r[1])[1]

    def get_min_y_including_sensor_radiuses(self):
        position_min_y = self.get_min_y()
        position_with_radius_min = min(self.get_sensor_positions_with_radius(), key=lambda r:r[1]-r[2])
        position_with_radius_min_y = position_with_radius_min[1] - position_with_radius_min[2]
        return min(position_min_y, position_with_radius_min_y)

    def get_max_y(self):
        return max(self.get_all_positions(), key=lambda r:r[1])[1]

    def get_max_y_including_sensor_radiuses(self):
        position_max_y = self.get_max_y()
        position_with_radius_max = max(self.get_sensor_positions_with_radius(), key=lambda r:r[1]+r[2])
        position_with_radius_max_y = position_with_radius_max[1] + position_with_radius_max[2]
        return max(position_max_y, position_with_radius_max_y)

    # Look for the distress beacon, which sits in a cell unexplored (.) on the map. Since we know there's only one
    # potential cell in the search space, we know that it must sit immediately outside the perimeter of the radius of a
    # beacon. Traverse the outside of each beacon in the cave and return the first (and only) candidate cell.
    def find_distress_beacon(self, min_x, max_x, min_y, max_y, print_progress=False):
        sensors = self.get_sensor_positions_with_radius()
        for sensor_i, sensor in enumerate(sensors):
            if print_progress:
                print('Sensor {}/{}: traversing perimeter'.format(sensor_i + 1, len(sensors)))

            perimeter_coords = get_diamond_perimeter((sensor[0], sensor[1]), sensor[2])
            perimeter_coords_count = len(perimeter_coords)

            for coord_i, coord in enumerate(perimeter_coords):
                x = coord[0]
                y = coord[1]
                if x < min_x or x > max_x or y < min_y or y > max_y:
                    # Out of bounds
                    continue

                if print_progress:
                    percentage = (coord_i + 1) / perimeter_coords_count * 100
                    print(' - Sensor {}/{}: inspecting coordinate x{} y{} (perimeter {:.2f}% explored)'.format(sensor_i + 1, len(sensors), x, y, percentage))

                if (
                    (x, y) not in self.get_all_positions() and
                    cave.is_coord_in_any_sensor_radius((x, y)) == False
                ):
                    # Found an unexplored cell!
                    return (x, y)

        return None


# Get a list of coordinates that surround a diamond. In other words, if you were
# to draw a diamond on a grid and trace the line that sits immediately outside
# it it.
def get_diamond_perimeter(center_coord, radius):
    x = center_coord[0]
    y = center_coord[1]
    north = (x, y + (radius + 1))
    east = (x + (radius + 1), y)
    south = (x, y - (radius + 1))
    west = (x - (radius + 1), y)

    coords = []

    # Start at North
    x2, y2 = north[0], north[1]

    # Travel North -> East
    while (x2, y2) != east:
        x2 += 1
        y2 -= 1
        coords.append((x2, y2))
    # Travel East -> South
    while (x2, y2) != south:
        x2 -= 1
        y2 -= 1
        coords.append((x2, y2))
    # Travel South -> West
    while (x2, y2) != west:
        x2 -= 1
        y2 += 1
        coords.append((x2, y2))
    # Travel West -> North
    while (x2, y2) != north:
        x2 += 1
        y2 += 1
        coords.append((x2, y2))

    return coords


def print_cave(cave, min_x = None, max_x = None, min_y = None, max_y = None):
    # Clear the terminal
    os.system('clear')

    min_x = cave.get_min_x_including_sensor_radiuses() if min_x is None else min_x
    max_x = cave.get_max_x_including_sensor_radiuses() if max_x is None else max_x
    min_y = cave.get_min_y_including_sensor_radiuses() if min_y is None else min_y
    max_y = cave.get_max_y_including_sensor_radiuses() if max_y is None else max_y

    for y in range(min_y - 1, max_y + 1):
        if y == min_y - 1:
            # Print x index start point
            print(' ' + str(min_x).rjust(len(str(max_y)) + 5))
            continue
        # Print y index down the left
        print(str(y).ljust(len(str(max_y)) + 5), end='')

        for x in range(min_x, max_x + 1):
            if (x, y) in cave.sensor_positions:
                print('S', end='')
            elif (x, y) in cave.beacon_positions:
                print('B', end='')
            elif cave.is_coord_in_any_sensor_radius((x, y)):
                print('#', end='')
            else:
                print('.', end='')
        print()

    print()

# Get the manhattan distance between two points (tuples) on a grid
# Example input: (1, 5), (10, 12)
# https://datascienceparichay.com/article/manhattan-distance-python/
def get_manhattan_distance(a_coord, b_coord):
    distance = 0
    for p_i, q_i in zip(a_coord, b_coord):
        distance += abs(p_i - q_i)

    return distance


# Given a coordinate, determine if it falls in the radius (diamond) of any sensor in the cave
# https://stackoverflow.com/a/10717542/526495
# http://jsfiddle.net/z98hr/
def is_coord_in_sensor_radius(target_coord, sensor_coord, sensor_radius):
    dx = abs(target_coord[0] - sensor_coord[0]);
    dy = abs(target_coord[1] - sensor_coord[1]);
    if (dx / sensor_radius + dy / sensor_radius <= 1):
        return True

    return False


def get_positions():
    sensor_positions = []
    beacon_positions = []

    with open('input.txt') as input_file:
        for line in input_file:
            # Replace all chars apart from 0-9 and - with a space
            line = re.sub('[^0-9-]', ' ', line)
            # Remove multiple spaces
            line = re.sub(' +', ' ', line.strip())
            # Set of 4 coords now looks like '0 1 -2 3'
            coords = line.split(' ')

            sensor_positions.append((int(coords[0]), int(coords[1])))
            beacon_positions.append((int(coords[2]), int(coords[3])))

    return (sensor_positions, beacon_positions)


def create_cave():
    sensor_positions, beacon_positions = get_positions()
    return Cave(sensor_positions, beacon_positions)


cave = create_cave()

# Set these vars according to the instructions
min_x = min_y = 0
max_x = max_y = 4000000

big_cave = max(cave.get_max_x(), cave.get_max_y()) >= 100
if big_cave == False:
    print_cave(cave, min_x, max_x, min_y, max_y)

distress_beacon_coordinate = cave.find_distress_beacon(min_x, max_x, min_y, max_y, big_cave == True)

print('-' * 50)
if distress_beacon_coordinate:
    print('Found an empty cell at coordinate x{} y{}, so it must contain the distress beacon.'.format(distress_beacon_coordinate[0], distress_beacon_coordinate[1]))
    tuning_frequency = distress_beacon_coordinate[0] * 4000000 + distress_beacon_coordinate[1]
    print('Tuning frequency: {}'.format(tuning_frequency))
else:
    print('Could not find distress beacon. There must be a bug.')
