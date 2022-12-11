import math
import time

class Monkey(object):
    def __init__(self, index):
        self.index = index
        self.items = []
        self.inspected_items_count = 0
        self.operation_eval = ''
        self.test_divisible_by = ''
        self.test_true_target = ''
        self.test_false_target = ''

    def __str__(self):
        output =  '== Monkey {} ==\n'.format(self.index)
        output += 'Items: {}\n'.format(self.items)
        output += 'Operation: new = {}\n'.format(self.operation_eval)
        output += 'Test: divisible by {}\n'.format(self.test_divisible_by)
        output += '  If true: throw to monkey {}\n'.format(self.test_true_target)
        output += '  If false: throw to monkey {}\n'.format(self.test_false_target)

        return output


def print_monkeys(monkeys):
    for monkey in monkeys:
        print(monkey)


def print_monkey_business(monkeys):
    for monkey in monkeys:
        print('Monkey {} -> items: {}, inspected_items_count: {}'.format(monkey.index, monkey.items, monkey.inspected_items_count))

    ordered_monkeys = sorted(monkeys, key=lambda x: x.inspected_items_count, reverse=True)
    monkey_business_score = ordered_monkeys[0].inspected_items_count * ordered_monkeys[1].inspected_items_count
    print('Monkey business score: {}'.format(monkey_business_score))


def assemble_monkeys():
    monkeys = []
    with open('input.txt') as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith('Monkey '):
                index = line[7:].replace(':', '')
                monkey = Monkey(index)
                monkeys.append(monkey)
            elif line.startswith('Starting items: '):
                monkey.items = [int(x) for x in line[16:].split(', ')]
                pass
            elif line.startswith('Operation: '):
                monkey.operation_eval = line[17:]
                pass
            elif line.startswith('Test: '):
                monkey.test_divisible_by = int(line[19:])
                pass
            elif line.startswith('If true: '):
                monkey.test_true_target = int(line[25:])
                pass
            elif line.startswith('If false: '):
                monkey.test_false_target = int(line[26:])
                pass

    return monkeys


def play_game(monkeys, rounds):
    # The items can get HUGE when we get to thousands of rounds. Performing
    # operations on those items is totally impractical – things get impossibly
    # slow (and calculations likely become erroneous). Luckily there's a trick
    # to make these items a lot smaller: calculating the lowest common multiple
    # (LCM) of all of the monkey's test_divisible_by values.
    #
    # We can then pass the LCM to pow() as the modulo operator. This just gives
    # us the remainder of the calculation rather than a HUGE number. Which is
    # totally adequate, as ultimately we don't care too much about the exact
    # values: we only care if the items are *divisible* by each monkey's
    # test_divisible_by. And the modulo remainder satisfies that requirement.
    lowest_common_multiple = math.lcm(*[m.test_divisible_by for m in monkeys])

    round_count = 1
    while round_count <= rounds:
        print('== Round {} =='.format(round_count))
        for monkey in monkeys:
            # print('Monkey {}:'.format(monkey.index))
            for item in monkey.items:
                # print('  Monkey inspects an item with a worry level of {}.'.format(item))
                if monkey.operation_eval == 'old * old':
                    item = pow(item, 2, lowest_common_multiple)
                else:
                    old = item
                    item = eval(monkey.operation_eval)
                # print('    Worry level operation eval is "{}". New value of {}.'.format(monkey.operation_eval, item))
                # print('    Monkey gets bored with item.')
                if item % monkey.test_divisible_by == 0:
                    # print('    Current worry level is divisible by {}.'.format(monkey.test_divisible_by))
                    # print('    Item with worry level {} is thrown to monkey {}.'.format(item, monkey.test_true_target))
                    monkeys[monkey.test_true_target].items.append(item)
                else:
                    # print('    Current worry level is not divisible by {}.'.format(monkey.test_divisible_by))
                    # print('    Item with worry level {} is thrown to monkey {}.'.format(item, monkey.test_false_target))
                    monkeys[monkey.test_false_target].items.append(item)
                monkey.inspected_items_count += 1
            monkey.items = []

        round_count += 1
        print_monkey_business(monkeys)
        print()

    return monkeys


# print(pow(10, 2, 21))
monkeys = assemble_monkeys()
print_monkeys(monkeys)
play_game(monkeys, 10000)
print_monkey_business(monkeys)
