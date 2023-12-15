from itertools import product
import re


def find_combos(spring, conti):
    combos = []
    for i, p in enumerate(product('.#', repeat = len(spring))):
        curr_spr = "".join(p)
        possible = curr_spr.count('#') == sum(conti)
        if possible:
            for i, char in enumerate(p):
                if (spring[i] != '?' and char != spring[i]):
                    possible = False
                    break
            if possible:
                i = 0
                for cont in conti:
                    while i < len(curr_spr) and curr_spr[i] != '#':
                        i += 1
                    j = 0
                    while i < len(curr_spr) and curr_spr[i] == '#':
                        j += 1
                        i += 1
                    if j != cont:
                        possible = False
                        break
                while i < len(curr_spr):
                    if(curr_spr[i] == '#'):
                        possible = False
                        break
                    i+=1
            if possible:
                combos.append(curr_spr)
    return combos

if __name__ == "__main__":
    puzzle_input = open("input/12.txt").readlines()
    springs = []
    contiguous = []
    for s in puzzle_input:
        s = s.strip()
        sprng, nums = s.split(' ')
        springs.append(sprng)
        contiguous.append(tuple(map(int, nums.split(','))))

    count = 0
    for i in range(len(springs)):
        count += len(find_combos(springs[i], contiguous[i]))
    print(count)
           