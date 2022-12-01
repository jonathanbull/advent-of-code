elf_calorie_counts = {}

# Get calorie counts for each elf
with open('data.txt') as input_file:
    elf_index = 1
    for line in input_file:
        line = line.strip()
        if line.isnumeric():
            elf_calorie_counts[elf_index] = elf_calorie_counts.get(elf_index, 0) + int(line)
        else:
            elf_index += 1

# Sort by calorie count DESC
elf_calorie_counts = dict(sorted(elf_calorie_counts.items(), key=lambda item: item[1], reverse=True))

# Output
print('--- Top 3 elves ---')
elf_calorie_count_sum = 0
for index in list(elf_calorie_counts)[:3]:
    print('Elf {}: {} calories'.format(index, elf_calorie_counts[index]))
    elf_calorie_count_sum += int(elf_calorie_counts[index])
print('')
print('Sum: {} calories'.format(elf_calorie_count_sum))
