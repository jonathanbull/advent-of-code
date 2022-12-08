def add_line_to_table(table, line):
    table.append([*line])


def print_table(table, add_scenic_score):
    for y, row in enumerate(table):
        for x, cell in enumerate(row):
            if add_scenic_score:
                scenic_score = get_scenic_score_for_cell(table, x, y)
                print('[{}]{} '.format(cell, scenic_score), end='')
            else:
                print('{}   '.format(cell), end='')
        print("\n")


def get_scenic_score_for_cell(table, x, y):
    target_row = table[y]
    target_column = [row[x] for row in table]
    target_cell = target_row[x]

    cells_looking_up = list(reversed(target_column[0:y]))
    cells_looking_right = target_row[x+1:]
    cells_looking_down = target_column[y+1:]
    cells_looking_left = list(reversed(target_row[:x]))

    # print('Target cell ({}, {}): {}'.format(x, y, target_cell))
    # print('Cells looking up: {}'.format(' '.join(cells_looking_up)))
    # print('Cells looking right: {}'.format(' '.join(cells_looking_right)))
    # print('Cells looking down: {}'.format(' '.join(cells_looking_down)))
    # print('Cells looking left: {}'.format(' '.join(cells_looking_left)))

    score = 1
    cell_groups = [cells_looking_up, cells_looking_right, cells_looking_down, cells_looking_left]
    for cell_group in cell_groups:
        group_score = 0
        for cell in cell_group:
            group_score +=1
            if cell >= target_cell:
                break
        if group_score == 0:
            return 0

        score *= group_score

    return score


def find_highest_scenic_score_in_table(table):
    highest_score = 0
    for y, row in enumerate(table):
        for x, _ in enumerate(row):
            score = get_scenic_score_for_cell(table, x, y)
            if score > highest_score:
                print('New highest score ({}, {}): {}'.format(x, y, score))
                highest_score = score

    return highest_score


table = []
with open('input.txt') as input_file:
    for line in input_file:
        add_line_to_table(table, line.strip())

# print_table(table, False)
# print_table(table, True)

highest_scenic_score_in_table = find_highest_scenic_score_in_table(table)

print('-' * 50)
print('Highest scenic score: {}'.format(highest_scenic_score_in_table))
