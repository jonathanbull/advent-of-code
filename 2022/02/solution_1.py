shape_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

shape_beats_shape = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}


def get_score_for_round(line):
    opponent_shape = shape_map[line[0]]
    my_shape = shape_map[line[2]]
    my_score = shape_scores[my_shape]

    print('Opponent chooses {}'.format(opponent_shape))
    print('I choose {} (+{})'.format(my_shape, my_score))

    if shape_beats_shape[my_shape] == opponent_shape:
        print('= Win (+6)')
        my_score += 6
    elif opponent_shape == my_shape:
        print('= Draw (+3)')
        my_score += 3
    else:
        print('= Loss (+0)')

    print('Total score for round: {}'.format(my_score))

    return my_score


total_score = 0
with open('input.txt') as input_file:
    for line in input_file:
        total_score += get_score_for_round(line.strip())
        print('')

print('-' * 20)
print('Total score: {}'.format(total_score))
