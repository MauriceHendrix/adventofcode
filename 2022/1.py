input = open('1.txt').readlines()

elves_totals = []
total = 0
for line in input:
    if line != '\n':
        total += int(line)
    else:
        elves_totals.append(total)
        total = 0

elves_totals.append(total)
print(f'elf with highest calories has {max(elves_totals)}')
elves_totals.sort()
print(f'top 3 elves have: {sum((elves_totals[-1], elves_totals[-2], elves_totals[-3]))}')