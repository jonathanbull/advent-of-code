shape_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

forced_outcome_map = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

shape_beats_shape = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

def get_score_for_round(line):
    opponent_shape = shape_map[line[0]]
    forced_outcome = forced_outcome_map[line[2]]

    if forced_outcome == 'lose':
        my_shape = shape_beats_shape[opponent_shape]
    elif forced_outcome == 'win':
        shape_beats_shape_reversed = dict((v,k) for k,v in shape_beats_shape.items())
        my_shape = shape_beats_shape_reversed[opponent_shape]
    else:
        my_shape = opponent_shape

    my_score = shape_scores[my_shape]

    print('Opponent chooses {}'.format(opponent_shape))
    print('I need to {}, so I choose {} (+{})'.format(forced_outcome, my_shape, my_score))

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
