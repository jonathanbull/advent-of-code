def get_pairs(line):
    pairs = line.split(',')
    pair_a_from_to = pairs[0].split('-')
    pair_b_from_to = pairs[1].split('-')

    pair_a_range = range(int(pair_a_from_to[0]), int(pair_a_from_to[1]) + 1)
    pair_b_range = range(int(pair_b_from_to[0]), int(pair_b_from_to[1]) + 1)

    return pair_a_range, pair_b_range


def range_overlaps_range(x, y):
    for number in x:
        if number in y:
            return True

    return False


pair_overlaps_the_other_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        print(line)

        pairs = get_pairs(line)
        pair_a_overlaps_pair_b = range_overlaps_range(pairs[0], pairs[1])
        pair_b_overlaps_pair_a = range_overlaps_range(pairs[1], pairs[0])

        if pair_a_overlaps_pair_b or pair_b_overlaps_pair_a:
            pair_overlaps_the_other_count += 1
            print('- pair overlaps the other')

        print('')


print('Pair overlaps the other count: {}'.format(pair_overlaps_the_other_count))
