def get_pairs(line):
    pairs = line.split(',')
    pair_a_from_to = pairs[0].split('-')
    pair_b_from_to = pairs[1].split('-')

    pair_a_range = range(int(pair_a_from_to[0]), int(pair_a_from_to[1]) + 1)
    pair_b_range = range(int(pair_b_from_to[0]), int(pair_b_from_to[1]) + 1)

    return pair_a_range, pair_b_range


def range_is_subset_of_range(x, y):
    for number in x:
        if number not in y:
            return False

    return True


pair_contains_the_other_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        print(line)

        pairs = get_pairs(line)
        pair_a_contains_pair_b = range_is_subset_of_range(pairs[0], pairs[1])
        pair_b_contains_pair_a = range_is_subset_of_range(pairs[1], pairs[0])

        if pair_a_contains_pair_b or pair_b_contains_pair_a:
            pair_contains_the_other_count += 1
            print('- pair contains the other')

        print('')


print('Pair contains the other count: {}'.format(pair_contains_the_other_count))
