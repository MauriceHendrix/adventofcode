from utility.timing import timing
from math import ceil

def find_horizontal_reflection(grd):
    rev_grid = list(reversed(grd))
    for i in range(ceil(len(grd)/2)):
        if(grd[:i+1] == list(reversed(grd[i+1:][:i+1]))):
            return i+1
        if(rev_grid[:i+1] == list(reversed(rev_grid[i+1:][:i+1]))):
            return len(grd)-1-i
    return 0
        
def find_horizontal_reflection2(grd):
    for i in range(len(grd)-1):
        if(grd[i] == grd[i+1]):
            found = True
            for j in range(1, min(i+1, len(grd)-i)):
                if(0 <= i-j and i+1+j < len(grd)):
                    if(grd[i-j] != grd[i+1+j]):
                        found = False
                        break
            if found:
                return i+1
    return 0


def off_by_1(l1, l2):
    if(len(l1) != len(l2)):
        return False
    diff = [[1 if l1[i][j] != l2[i][j] else 0 for j in range(len(l1[i]))] for i in range(len(l1))]
    return sum(map(sum, diff)) == 1

def find_reflection_part2(grd):
    rev_grid = list(reversed(grd))
    for i in range(ceil(len(grd)/2)):
        if(off_by_1(grd[:i+1], list(reversed(grd[i+1:][:i+1])))):
            return i+1
        if(off_by_1(rev_grid[:i+1], list(reversed(rev_grid[i+1:][:i+1])))):
            return len(grd)-1-i
    return 0

@timing
def part1(puzzle_input):
    total_sum = 0
    for map_input in puzzle_input:
        grid = list(map(list, map_input.splitlines()))
        grid_t = [[p[i] for p in grid] for i in range(len(grid[0]))]
        above = find_horizontal_reflection(grid)
        left = find_horizontal_reflection(grid_t)
        total_sum += left + 100 * above
    return total_sum

@timing
def part1b(puzzle_input):
    total_sum = 0
    for map_input in puzzle_input:
        grid = list(map(list, map_input.splitlines()))
        grid_t = [[p[i] for p in grid] for i in range(len(grid[0]))]
        above = find_horizontal_reflection2(grid)
        left = find_horizontal_reflection2(grid_t)
        total_sum += left + 100 * above
    return total_sum

def part2(puzzle_input):
    total_sum = 0
    for map_input in puzzle_input:
        grid = list(map(list, map_input.splitlines()))
        grid_t = [[p[i] for p in grid] for i in range(len(grid[0]))]
        above = find_reflection_part2(grid)
        left = find_reflection_part2(grid_t)
        total_sum += left + 100 * above
    return total_sum
    
if __name__ == "__main__":
    puzzle_input = open("input/13.txt").read().split('\n\n')
    print(part1(puzzle_input))
    print(part1b(puzzle_input))
    print(part2(puzzle_input))
