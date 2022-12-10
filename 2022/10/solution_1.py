interesting_cycles = [20, 60, 100, 140, 180, 220]
interesting_signal_strength_sum = 0

def log_cycle(cycle_number, x):
    global interesting_signal_strength_sum
    print('Logging cycle {}, x: {}'.format(cycle_number, x))
    if cycle_number in interesting_cycles:
        signal_strength = (cycle_number * x)
        print('Interesting cycle! x: {}, signal_strength: {}'.format(x, signal_strength))
        interesting_signal_strength_sum += signal_strength


cycle_number = 0
x = 1
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        print('==' + line + '==')
        cycle_number += 1
        log_cycle(cycle_number, x)

        if line.startswith('addx '):
            for i in range(0, 1):
                cycle_number += 1
                log_cycle(cycle_number, x)
            value = int(line[5:])
            x += value


print('Cycle count: {}'.format(cycle_number))
print('x: {}'.format(x))
print('Sum of x at interesting cycles {}: {}'.format(interesting_cycles, interesting_signal_strength_sum))
