import re

# Part one
total = 0
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        numbers = re.sub(r"\D", '', line)
        total += (int(numbers[0] + numbers[-1]))
print('--- Part one ---')
print(total)

# Part two
