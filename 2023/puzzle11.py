import itertools

def shortest_path(galaxy_map, pair):
    print(pair, galaxy_map[pair[0][0]][pair[0][1]], galaxy_map[pair[1][0]][pair[1][1]])
    return 0

def part1(galaxy_map, galaxy_pos):
    total_sum = 0
    for pair in itertools.combinations(galaxy_pos, 2):
        print(pair)
        total_sum += shortest_path(galaxy_map, pair)
    return total_sum

def part2(galaxy_map):
    return ''

if __name__ == "__main__":
    puzzle_input = list(map(list, open("input/11.txt").read().splitlines()))
    galaxy_map = []
    galaxy_pos = []
    
    i=0
    while i< len(puzzle_input):
        for _ in range(2 if all([g=='.'for g in puzzle_input[i]]) else 1):
            j = 0
            new_line = []
            while j < len(puzzle_input):
                for _ in range(2 if all([puzzle_input[k][j]=='.' for k in range(len(puzzle_input))]) else 1):
                    new_line.append(puzzle_input[i][j])
                j+=1
            galaxy_map.append(new_line)
        i+=1
    for i, ln in enumerate(galaxy_map):
        for j, g in enumerate(ln):
            if g == '#':
                galaxy_pos.append((i,j))            
    #print(part1(galaxy_map, galaxy_pos))
    #print(galaxy_map)
    #print(galaxy_pos)

    print(shortest_path(galaxy_map, ((11,0),(11,5))))