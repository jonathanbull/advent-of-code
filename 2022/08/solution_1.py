def add_line_to_table(table, line):
    table.append([*line])


def print_table(table, highlight_visible):
    for y, row in enumerate(table):
        for x, cell in enumerate(row):
            if highlight_visible:
                if is_cell_visible_in_table(table, x, y):
                    print('[{}] '.format(cell), end='')
                else:
                    print(' {}  '.format(cell), end='')
            else:
                print('{}   '.format(cell), end='')
        print("\n")


def is_cell_visible_in_table(table, x, y):
    target_row = table[y]
    target_column = [row[x] for row in table]
    target_cell = target_row[x]

    cells_above = target_column[0:y]
    cells_right = target_row[x+1:]
    cells_below = target_column[y+1:]
    cells_left = target_row[:x]

    # print('Target cell ({}, {}): {}'.format(x, y, target_cell))
    # print('Cells above: {}'.format(' '.join(cells_above)))
    # print('Cells right: {}'.format(' '.join(cells_right)))
    # print('Cells below: {}'.format(' '.join(cells_below)))
    # print('Cells left: {}'.format(' '.join(cells_left)))

    cell_groups = [cells_above, cells_right, cells_below, cells_left]
    for cell_group in cell_groups:
        if all(cell < target_cell for cell in cell_group):
            return True

    return False


def count_cells_visible_in_table(table):
    count = 0
    for y, row in enumerate(table):
        for x, _ in enumerate(row):
            if is_cell_visible_in_table(table, x, y):
                count += 1

    return count


table = []
with open('input.txt') as input_file:
    for line in input_file:
        add_line_to_table(table, line.strip())

# print_table(table, False)
# print_table(table, True)

cells_visible_count = count_cells_visible_in_table(table)

print('-' * 50)
print('Total trees visible: {}'.format(cells_visible_count))
