from itertools import product
from collections import deque
import re



def matches(cmb, conti):
    cmb = "".join(cmb)
    return tuple(map(len, re.findall('#+', cmb))) == conti

def get_combos(spring, conti):
    expected_hashes = sum(conti)
    combos = deque([spring])
    for i in range(len(spring)):
        if spring[i] == '?':
            for _ in range(len(combos)):
                cmb = combos.popleft()
                for char in ('.', '#'):
                    combos.append(cmb[:i] + char + cmb[i+1:])
    return filter(lambda c: matches(c,conti), combos)
    
def find_combos(spring, conti):
    combos = []
    for i, p in enumerate(get_combos(spring, conti)):
        curr_spr = "".join(p)
        possible = curr_spr.count('#') == sum(conti)
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

def part1(springs, contiguous):
    count = 0
    for i in range(len(springs)):
         count += len(find_combos(springs[i], contiguous[i]))
    return count
    
if __name__ == "__main__":
    puzzle_input = open("input/12.txt").readlines()
    springs = []
    contiguous = []
    for s in puzzle_input:
        s = s.strip()
        sprng, nums = s.split(' ')
        springs.append(sprng)
        contiguous.append(tuple(map(int, nums.split(','))))

    print(part1(springs, contiguous))

    for i, spring in enumerate(springs):
        springs[i] = (spring+'?')*5
        springs[i] = springs[i][:-1]

    for i in range(len(contiguous)):
        contiguous[i]*= 5
