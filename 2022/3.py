import string
input = open('3.txt').readlines()

priorities = {char: i for i, char in enumerate(string.ascii_lowercase, start=1)} | {char: i for i, char in enumerate(string.ascii_uppercase, start=27)}

priorities_sum = 0
for line in input:
    compartment1 = line[:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):]
    in_common = set(compartment1).intersection(set(compartment2))
    assert len(in_common) == 1
    common_char = in_common.pop()
    #print((common_char[0], priorities[common_char[0]]))
    priorities_sum += priorities[common_char[0]]
print(priorities_sum)

priorities_sum = 0
for i in range(0, len(input), 3):
    line1 = input[i].strip()
    line2 = input[i+1].strip()
    line3 = input[i+2].strip()
    in_common = set(line1).intersection(set(line2)).intersection(set(line3))
    assert len(in_common) == 1
    common_char = in_common.pop()
    priorities_sum += priorities[common_char[0]]
print(priorities_sum)