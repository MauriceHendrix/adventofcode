from timing import timing


@timing
def part1(puzzle_input: list[str]):
    return 'todo'


@timing
def part2(puzzle_input: list[str]):
    return 'todo'


if __name__ == "__main__":
    puzzle_input = open("input/1.txt").readlines()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
