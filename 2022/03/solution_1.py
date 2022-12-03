import string

def get_common_items(rucksack_contents):
    compartment_a, compartment_b = rucksack_contents[:len(rucksack_contents)//2], rucksack_contents[len(rucksack_contents)//2:]

    return ''.join(set(compartment_a).intersection(compartment_b))


def get_priority_for_item(item):
    if item.isupper():
        return string.ascii_uppercase.index(item) + 27

    return string.ascii_lowercase.index(item) + 1


total_priority = 0
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        print(line)
        common_items = get_common_items(line)

        for item in common_items:
            priority = get_priority_for_item(item)
            print('Common item: {}, priority: {}'.format(common_items, priority))
            total_priority += priority

        print('')


print('Sum of priorities: {}'.format(total_priority))
