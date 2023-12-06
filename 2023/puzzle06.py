from utility.timing import timing

@timing
def part1(times, distances):
    totals = 1
    for time, reccord in zip(times, distances):
        count_win_options = 0
        for i in range(1, time):
            if i*(time-i) > reccord:
                count_win_options += 1
        totals *= count_win_options
        count_win_options = 0
    return totals

if __name__ == "__main__":
    puzzle_input = open("input/06.txt").read().splitlines()
    times = list(map(int, puzzle_input[0].replace('Time:', '').strip().split()))
    distances = list(map(int, puzzle_input[1].replace('Distance:', '').strip().split()))
    print(part1(times, distances))

    time = int(puzzle_input[0].replace('Time:', '').replace(' ', ''))
    distance = int(puzzle_input[1].replace('Distance:', '').replace(' ', ''))
    print(part1((time,), (distance,)))