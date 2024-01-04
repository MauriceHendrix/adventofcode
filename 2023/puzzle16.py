def reflect(direction, mirror):
    if mirror == '/':
        match direction:
            case '>':
                direction = '^'
            case '<':
                direction = 'v'
            case 'v':
                direction = '<'
            case '^':
                direction = '>'
    elif mirror == '\\':
        match direction:
            case '>':
                direction = 'v'
            case '<':
                direction = '^'
            case 'v':
                direction = '>'
            case '^':
                direction = '<'
    return direction

def move(i, j, direction):
    match direction:
        case '>':
            j += 1
        case '<':
            j -= 1
        case 'v':
            i += 1
        case '^':
            i -= 1
    return i, j, direction

def propagate(beam, energised, ctr):
    i, j, direction = beam
    energised[i][j] = True
    return_beams = []

    if ctr[i][j] == '|' and direction in ('>', '<'):
        return_beams.append(move(i, j, '^'))
        return_beams.append(move(i, j, 'v'))
    elif ctr[i][j] == '-' and direction in ('^', 'v'):
        return_beams.append(move(i, j, '>'))
        return_beams.append(move(i, j, '<'))
    else:
        return_beams.append(move(i, j, reflect(direction, ctr[i][j])))
    return [b for b in return_beams if b[0]>= 0 and b[1] >= 0 and b[0] <len(ctr[0]) and b[1] < len(ctr)]

def part1(ctr, start):
    energised = [[False for _ in range(len(ctr[0]))] for __ in range(len(ctr))]
    state_seen = {}
    beams = [start]
    while(len(beams) > 0):
        beam = beams.pop()
        if beam not in state_seen:
            state_seen[beam] = True
            beams.extend(propagate(beam, energised, ctr))
    return sum(sum(eln) for eln in energised)

def part2(ctr):
    max_sum = 0
    #top and bottom edge
    for j in range(len(ctr[0])):
        max_sum = max(max_sum, part1(ctr, (0, j, 'v')), part1(ctr, (len(ctr)-1, j, '^')))
    #left and right edge
    for i in range(len(ctr[0])):
        max_sum = max(max_sum, part1(ctr, (i, 0, '>')), part1(ctr, (i, len(ctr[0])-1, '<')))
    return max_sum

if __name__ == "__main__":
    puzzle_input = open("input/16.txt").read().strip().split('\n')
    print(part1(puzzle_input, (0, 0, '>')))
    print(part2(puzzle_input))
