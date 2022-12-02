import time

shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

shape_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

def get_score_for_round(line):
    opponent_shape = shape_map[line[0]]
    opponent_score = shape_scores[opponent_shape]
    my_shape = shape_map[line[2]]
    my_score = shape_scores[my_shape]

    print('Opponent chooses {} ({})'.format(opponent_shape, opponent_score))
    print('I choose {} ({})'.format(my_shape, my_score))

    if (
        (my_shape == 'rock' and opponent_shape == 'scissors') or
        (my_shape == 'paper' and opponent_shape == 'rock') or
        (my_shape == 'scissors' and opponent_shape == 'paper')
    ):
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
        print('Total score: {}'.format(total_score))
        print('')
        # time.sleep(1)

print('-' * 20)
print('Total score: {}'.format(total_score))
