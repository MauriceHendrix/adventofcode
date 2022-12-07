import string
input = open('4.txt').readlines()

count = 0
for line in input:
    pair = line.strip().split(',')
    elf1 = [int(n) for n in pair[0].split('-')]
    elf2 = [int(n) for n in pair[1].split('-')]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]) and not (elf1[0] == elf2[0] and elf1[1] == elf2[1]):
        count += 1

print(count)

count = 0
for line in input:
    pair = line.strip().split(',')
    elf1 = [int(n) for n in pair[0].split('-')]
    elf2 = [int(n) for n in pair[1].split('-')]
    if (elf2[0] <= elf1[1] and elf2[1] >= elf1[0]) or (elf1[0] <= elf2[1] and elf1[1] >= elf2[0]):
        count += 1

print(count)