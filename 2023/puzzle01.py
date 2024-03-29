from utility.timing import timing
from functools import reduce


@timing
def part1(puzzle_input: list[str]):
    total = 0
    for cal in puzzle_input:
        lineNrStr = ''
        for char in cal:
            if char.isnumeric():
                lineNrStr += str(char)
        total += int(lineNrStr[0] + lineNrStr[-1])
    return total


@timing
def part1b(puzzle_input: list[str]):
        return reduce(lambda l1, l2: l1 + int(l2[0] + l2[-1]),
                      map(lambda ln: list(filter(lambda s: s.isnumeric(), ln)), puzzle_input), 0)


@timing
def part2(puzzle_input: list[str]):
    digit_strs = {'one': 1, 'two': 2, 'three': 3,
                  'four': 4, 'five': 5, 'six': 6,
                  'seven': 7, 'eight': 8, 'nine': 9}
    total = 0
    for cal in puzzle_input:
        lineNrStr = ''
        for i in range(len(cal)):
            if cal[i].isnumeric():
                lineNrStr += str(cal[i])
            elif cal[i] in ('o', 't', 'f', 's', 'e', 'n'):
                for numstr, numval in digit_strs.items():
                    if cal[i:].startswith(numstr):
                        lineNrStr += str(digit_strs[numstr])
        total += int(lineNrStr[0] + lineNrStr[-1])
    return total


if __name__ == "__main__":
    puzzle_input = open("input/01.txt").readlines()
    print(part1(puzzle_input))
    print(part1b(puzzle_input))
#    print(part2(puzzle_input))
