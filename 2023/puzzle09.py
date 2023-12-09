
def calculate_next(history):
    compare = history
    differences = []
    i = -1
    while(compare == history or sum(map(abs, differences[i])) > 0):
        i += 1
        differences.append([None] * (len(compare) -1))
        for j in range(1, len(compare)):
            differences[i][j-1] = compare[j] - compare[j-1]
        compare = differences[i]
    differences[-2].append(differences[-2][-1])
    for i in range(-3, -(len(differences) +1), -1):
        differences[i].append(differences[i+1][-1] + differences[i][-1])
    return history[-1] + differences[0][-1]

def part1(histories):
    return sum(map(calculate_next, histories))

def part2(histories):
    return sum(map(calculate_next, map(list, map(reversed, histories))))

if __name__ == "__main__":
    puzzle_input = [list(map(int, num.split())) for num in open("input/09.txt").read().splitlines()]
    print(part1(puzzle_input))
    print(part2(puzzle_input))
