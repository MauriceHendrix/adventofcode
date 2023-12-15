import itertools

def shortest_path(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

def calc_sum_galgxypaths(puzzle_input, times):
    galaxy_pos = []
    
    i2=0
    for i, line in enumerate(puzzle_input):
        if('#' in str(line)):
            j2 = 0
            for j, g in enumerate(line):
                if(g=='#'):
                    galaxy_pos.append((i2,j2))
                if all([puzzle_input[k][j]=='.' for k in range(len(puzzle_input))]):
                    j2+=(times-1)
                j2+=1
        else:
            i2+=(times-1)
        i2 += 1

    total_sum = 0
    for pair in itertools.combinations(galaxy_pos, 2):
        total_sum += shortest_path(pair)
    return total_sum

if __name__ == "__main__":
    puzzle_input = list(map(list, open("input/11.txt").read().splitlines()))
    print(calc_sum_galgxypaths(puzzle_input, 2))
    print(calc_sum_galgxypaths(puzzle_input, 1000000))
