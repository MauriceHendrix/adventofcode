
def calculate_size(puzzle_input):
    minx, maxx, miny, maxy, x, y, tiles = 0, 0, 0, 0, 0, 0, {}
    dir_moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    def mark_edge(start):
        def get_neigbours(start):
            x,y = start
            neigbours = []
            # up
            if y-1 >= miny-1 and ((x, y-1) not in tiles or not tiles[(x, y-1)][0]):
                neigbours.append((x, y-1))
            # down
            if y+1 <= maxy+1 and ((x, y+1) not in tiles or not tiles[(x, y+1)][0]):
                neigbours.append((x, y+1))
            # left
            if x-1 >= minx-1 and ((x-1, y) not in tiles or not tiles[(x-1, y)][0]):
                neigbours.append((x-1, y))
            # right
            if x+1 <= maxx+1 and ((x+1, y) not in tiles or not tiles[(x+1, y)][0]):
                neigbours.append((x+1, y))    
            return neigbours
        x, y = start
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            tiles[current] = (False, True)
            if current not in visited:
                visited.add(current)
                stack.extend(get_neigbours(current))        
                
        
    # record dug tiles
    for direction, length, colour in puzzle_input:
        for _ in range(int(length)):
            x, y = x + dir_moves[direction][0], y + dir_moves[direction][1]
            minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
            tiles[(x, y)] = (True, False)
    # add non-dug tiles
    for x in range(minx-1, maxx+2):
        tiles[x, miny-1] = (False, True)
        tiles[x, maxy+1] = (False, True)
    for y in range(miny-1, maxy+2):
        tiles[minx-1, y] = (False, True)
        tiles[maxx+1, y] = (False, True)

    mark_edge((minx-1, miny-1))
#    for y in range(miny-1, maxy+2):
#        for x in range(minx-1, maxx+2):
#            dug, path = tiles.get((x,y), (False, False))
#            print('#' if dug else '*' if path else '.', end='')
#        print()

    xlen = abs(minx) + abs(maxx) +1
    ylen = abs(miny) + abs(maxy) +1
    # dug out num = while field - nun doug-out
    return (xlen * ylen) -  sum(1 for t in tiles.items() if t[1][1] and not t[0][0] in(minx-1, maxx+1) and not  t[0][1] in (miny-1, maxy+1))
    
if __name__ == "__main__":
    puzzle_input = [line.split() for line in open("input/18.txt").readlines()]
    print(calculate_size(puzzle_input))
#    print(puzzle_input[0])
    direction_nums = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    puzzle_input2 = []
    for p in puzzle_input:
        direction = direction_nums[p[2][-2]]
        p = p[2][2:-2]
        puzzle_input2.append((direction, int(p, 16), 0))
    
    print(calculate_size(puzzle_input2))