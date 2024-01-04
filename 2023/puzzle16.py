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

def part1(ctr):
    energised = [[False for _ in range(len(ctr[0]))] for __ in range(len(ctr))]
    state_seen = {}
    beams = [(0, 0, '>')]
    while(len(beams) > 0):
        beam = beams.pop()
        if beam not in state_seen:
            state_seen[beam] = True
            beams.extend(propagate(beam, energised, ctr))
    return sum(sum(eln) for eln in energised)


if __name__ == "__main__":
    puzzle_input = open("input/16.txt").read().strip().split('\n')
    print(part1(puzzle_input))
