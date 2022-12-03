import string

def get_common_items(lines):
    return set.intersection(*map(set, lines))

def get_priority_for_item(item):
    if item.isupper():
        return string.ascii_uppercase.index(item) + 27

    return string.ascii_lowercase.index(item) + 1


def chunk_lines(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i:i + n]


total_priority = 0
with open('input.txt') as input_file:
    lines = []
    for line in input_file:
        line = line.strip()
        if line:
            lines.append(line)

    chunked_lines = chunk_lines(lines, 3)
    for line_chunk in chunked_lines:
        print(line_chunk)
        common_items = get_common_items(line_chunk)
        for item in common_items:
            priority = get_priority_for_item(item)
            print('Common item: {}, priority: {}'.format(common_items, priority))
            total_priority += priority

        print('')


print('Sum of priorities: {}'.format(total_priority))
