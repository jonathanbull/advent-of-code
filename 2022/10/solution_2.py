def print_cycle(cycle_number, x):
    current_pixel = 39 if cycle_number % 40 == 0 else (cycle_number % 40 - 1)
    sprite = [x-1, x, x+1]
    if current_pixel in sprite:
        print('#', end='')
    else:
        print('.', end='')

    if current_pixel == 39:
        print()


cycle_number = 0
x = 1
print('-' * 50)
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        cycle_number += 1
        print_cycle(cycle_number, x)

        if line.startswith('addx '):
            for i in range(0, 1):
                cycle_number += 1
                print_cycle(cycle_number, x)
            value = int(line[5:])
            x += value

print()
print('-' * 50)
print('Cycle count: {}'.format(cycle_number))
print('x: {}'.format(x))
