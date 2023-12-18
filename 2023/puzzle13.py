def find_horizontal_reflection(puzzle_input):
    for i in range(len(puzzle_input)):
        j=0
        found = i > 0
        while j < i and i+1+j < len(puzzle_input):
            if not puzzle_input[i-j]==puzzle_input[i+1+j]:
                found = False
                break
            j+=1
        if found:
            return(i+1, i+2)
    return 0

def part1(map1, map2):
    left = min(*find_horizontal_reflection(map1))
    above = min(*find_horizontal_reflection(map2))
    return left + 100 * above

if __name__ == "__main__":
    puzzle_input = open("input/13.txt").read().splitlines()
    puzzle_input = open("input/13.txt").read().split('\n\n')
    map1 = puzzle_input[0].splitlines()
    map1 = [[p[i] for p in map1] for i in range(len(map1[0]))]
    map2 = puzzle_input[1].splitlines()
    left = min(*find_horizontal_reflection(map1))
    above = min(*find_horizontal_reflection(map2))
    print(part1(map1, map2))
