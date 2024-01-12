
if __name__ == "__main__":
    puzzle_input = [line.split() for line in open("input/18.txt").readlines()]
    minx, maxx, miny, maxy = 0, 0, 0, 0
    curx, curx, cury, cury = 0, 0, 0, 0
    for ln in puzzle_input:
        match ln[0]:
            case 'R':
                curx += int(ln[1])
                maxx = max(maxx, curx)
            case 'L':
                curx -= int(ln[1])
                minx = min(minx, curx)
            case 'U':
                cury -= int(ln[1])
                miny = min(miny, cury)
            case 'D':
                cury += int(ln[1])
                maxy = max(maxy, cury)
    print(minx, maxx, miny, maxy)
    x,y = abs(minx), abs(miny)
    grid = [['.' for _ in range(abs(x) + abs(maxx) +1)] for __ in range(abs(y) + abs(maxy) +1)]
    grid[y][x] = '#'
    for ln in puzzle_input:
        for _ in range(int(ln[1])):
            match ln[0]:
                case 'R':
                        x += 1
                        grid[y][x] = '-'
                case 'L':
                        x -= 1
                        grid[y][x] = '-'
                case 'U':
                        y -= 1
                        grid[y][x] = '|'
                case 'D':
                        y += 1
                        grid[y][x] = '|'

    print(["".join(g) for g in grid])
    
    count = 0
    for y in range(len(grid)):
        inside = False
        for x in range(len(grid[y])):
            if grid[y][x] == '|':
                inside = not(inside)
            if inside or grid[y][x] in ('|', '-'):
                grid[y][x] = '#'
                count += 1
    #print()
    #print(["".join(g) for g in grid])
    print(count)