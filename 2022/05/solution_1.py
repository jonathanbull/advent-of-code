def get_stacks(input_file):
    stacks = {}
    for line in input_file:
        if '[' not in line:
            # We've reached the end of the stack data
            return stacks

        stack_number = 1
        for index, char in enumerate(list(line)):
            if index == 1 or ((index - 1) % 4 == 0):
                if char.isalpha():
                    if stack_number in stacks:
                        stacks[stack_number].insert(0, char)
                    else:
                        stacks[stack_number] = [char]

                stack_number += 1

    return stacks


def process_instruction(stacks, line):
    clean_line = line.replace('move ', '').replace(' from ', '/').replace(' to ', '/').strip()
    instructions = clean_line.split('/')
    move_quantity = int(instructions[0])
    move_from = int(instructions[1])
    move_to = int(instructions[2])

    for _ in range(move_quantity):
        stacks[move_to].append(stacks[move_from].pop())


def print_stacks(stacks):
    for number, crates in sorted(stacks.items()):
        print('Stack {} contains: {}'.format(number, crates))


def get_top_crates(stacks):
    top_crates = []
    for _, crates in sorted(stacks.items()):
        top_crates.append(crates[-1])

    return top_crates


with open('input.txt') as input_file:
    stacks = get_stacks(input_file)
    print_stacks(stacks)

    for line in input_file:
        if 'move ' in line:
            print()
            print(line)
            process_instruction(stacks, line)
            print_stacks(stacks)

    print()
    print('Finished arranging.')
    print()

    top_crates = get_top_crates(stacks)
    print('Top crates are: {}'.format(''.join(top_crates)))
