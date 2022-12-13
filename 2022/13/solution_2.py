import copy
from functools import cmp_to_key

class Pair(object):
    def __init__(self, index):
        self.index = index
        self.input_left = None
        self.input_right = None

    def inputs_filled(self):
        return self.input_left is not None and self.input_right is not None

    def inputs_in_correct_order(self):
        return compare_inputs(self.input_left, self.input_right)

    def __str__(self):
        return 'Pair {} -> {} | {}.'.format(self.index, self.input_left, self.input_right)


def compare_inputs(input_a, input_b, recursion_level = 0):
    # Avoid any modification of the original inputs
    input_a = copy.copy(input_a)
    input_b = copy.copy(input_b)

    print(' ' * (recursion_level * 2), end='')
    print('- Compare {} vs {}'.format(input_a, input_b))

    # Pad input_a so that it's the same size as input_b
    input_a += [None] * (len(input_b) - len(input_a))

    for level, left_v in enumerate(input_a):
        right_v = None
        if isinstance(input_b, list) and level < len(input_b):
            right_v = input_b[level]

        if isinstance(left_v, list) and len(left_v) == 1 and isinstance(right_v, list) and len(right_v) == 1:
            left_v = left_v[0]
            right_v = right_v[0]

        # Indent
        print(' ' * (recursion_level * 2), end='')
        print('  - Compare {} vs {} (level {} of recursion)'.format(left_v, right_v, recursion_level))

        if left_v is None and right_v is not None:
            print(' ' * (recursion_level * 2), end='')
            print('    - Left side ran out of items, so inputs are in the right order')
            return True
        elif left_v is not None and right_v is None:
            print(' ' * (recursion_level * 2), end='')
            print('    - Right side ran out of items, so inputs are not in the right order')
            return False
        elif isinstance(left_v, list) == False and isinstance(right_v, list) == False:
            if left_v < right_v:
                print(' ' * (recursion_level * 2), end='')
                print('    - Left side is smaller, so inputs are in the right order')
                return True
            elif left_v == right_v:
                print('  - Left side is the same as right side, continuing')
                pass
            else:
                print(' ' * (recursion_level * 2), end='')
                print('    - Right side is smaller, so inputs are not in the right order')
                return False

        if isinstance(left_v, list) == True and isinstance(right_v, list) == True and left_v != right_v:
            print('Returning val')
            # print(left_v)
            return compare_inputs(left_v, right_v, recursion_level + 1)

        if isinstance(left_v, list) == True and isinstance(right_v, list) == False:
            print(' ' * (recursion_level * 2), end='')
            print('    - Mixed types, convert right to [{}] and retry comparison'.format(right_v))
            return compare_inputs(left_v, [right_v], recursion_level + 1)

        if isinstance(left_v, list) == False and isinstance(right_v, list) == True:
            print(' ' * (recursion_level * 2), end='')
            print('    - Mixed types, convert left to [{}] and retry comparison'.format(left_v))
            return compare_inputs([left_v], right_v, recursion_level + 1)

    return False


def compare_inputs_sort_asc(input_a, input_b):
    print('- Sort compare: {} vs {}'.format(input_a, input_b))
    return -1 if compare_inputs(input_a, input_b) else 1


pairs = []
with open('input.txt') as pair_file:
    pair = Pair(1)

    for line in pair_file:
        line = line.strip()
        if line:
            if pair.input_left is None:
                pair.input_left = eval(line)
            elif pair.input_right is None:
                pair.input_right = eval(line)

            if pair.inputs_filled():
                pairs.append(pair)
                # Start a new pair
                pair = Pair(pair.index + 1)

decoder_packet_a = [[2]]
decoder_packet_b = [[6]]

packets = [decoder_packet_a, decoder_packet_b]

for pair in pairs:
    packets.append(pair.input_left)
    packets.append(pair.input_right)

packets_ordered = sorted(packets, key=cmp_to_key(compare_inputs_sort_asc))

print()
print('-' * 50)

decoder_packet_a_pos = None
decoder_packet_b_pos = None
for i, packet in enumerate(packets_ordered):
    position = i + 1
    if packet == decoder_packet_a:
        decoder_packet_a_pos = position
        print('Decoder packet A found at position {}'.format(position))
    elif packet == decoder_packet_b:
        decoder_packet_b_pos = position
        print('Decoder packet B found at position {}'.format(position))

print('Positions multiplied: {}'.format(decoder_packet_a_pos * decoder_packet_b_pos))
