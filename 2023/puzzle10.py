class Node:
    def __init__(self, tile, i, j):
        self.tile, self.i, self.j, self.connected_to, self.enclosed = tile, i, j, [], True

    def __repr__(self):
        return f'({self.i},{self.j}:{self.tile}: {"I" if self.enclosed else "O"})'

    
def dfs_cycle(visited, node, pathlength, pathlengths):  #function for dfs 
    stack = []
    stack.append((node, pathlength))
    while len(stack)> 0 and node != start:
        node, pathlength = stack.pop()
        if node not in visited:
            pathlengths.setdefault(node, []).append(pathlength)
            visited.add(node)
            for neighbour in node.connected_to:
                stack.append((neighbour, pathlength+1))


def get_neighbours(node, puzzle_input, pathlengths):
    neighbours = []
    if(node.i > 0):
        if (puzzle_input[node.i-1][node.j] not in pathlengths):
            neighbours.append(puzzle_input[node.i-1][node.j])
    if(node.i < len(puzzle_input) -1):
        if (puzzle_input[node.i+1][node.j] not in pathlengths):
            neighbours.append(puzzle_input[node.i+1][node.j])
    if(node.j > 0):
        if (puzzle_input[node.i][node.j-1] not in pathlengths):
            neighbours.append(puzzle_input[node.i][node.j-1])
    if(node.j < len(puzzle_input[node.i]) -1):
        if (puzzle_input[node.i][node.j+1] not in pathlengths):
            neighbours.append(puzzle_input[node.i][node.j+1])
    return neighbours


def find_cycle_pathlengths(start):
    pathlengths = {}

    for connected in start.connected_to:
        visited = set()
        dfs_cycle(visited, connected, 1, pathlengths)
    return pathlengths

def dfs_find_non_connected(puzzle_input, start, pathlengths):
    if start in pathlengths:
        return
    visited = set()
    stack = [(False, start)]
    while len(stack)> 0:
        on_squeeze, node = stack.pop()
        if node not in visited:
            visited.add(node)
            if not node.enclosed:
                start.enclosed = False
                for v in visited:
                    v.enclosed = False
                return
            for neighbour in get_neighbours(node, puzzle_input, pathlengths):
                stack.append((False, neighbour))

def part1(start):
    pathlengths = find_cycle_pathlengths(start)
    return max(filter(lambda x: len(x) ==2 and x[0] == x[1], pathlengths.values()))[0]

def part2(start, puzzle_input, adj_mattr):
    # find cycle
    pathlengths = find_cycle_pathlengths(start)
    pathlengths[start] = True
    for p in puzzle_input[0]:
        p.enclosed = False
    for p in puzzle_input[-1]:
        p.enclosed = False
    for i in range(len(puzzle_input)):
        puzzle_input[i][0].enclosed = False
        puzzle_input[i][-1].enclosed = False



    for i in range(len(puzzle_input)):
        is_inside = False
        for j in range(len(puzzle_input[i])):
            if(puzzle_input[i][j].tile in('|', 'L', 'J')) and puzzle_input[i][j] in pathlengths:
                is_inside = not(is_inside)
            if(not is_inside):
                puzzle_input[i][j].enclosed = False


    return sum([len([p for p in ln if p.enclosed and p not in pathlengths]) for ln in puzzle_input])

if __name__ == "__main__":
    def val_ind(i, j):
        return 0 <= i < len(puzzle_input) and 0 <= j < len(puzzle_input[i])
        
    def connect_north(i,j):
        if(val_ind(i-1, j) and puzzle_input[i-1][j].tile in ('|', '7', 'F', 'S')):
            puzzle_input[i-1][j].connected_to.append(puzzle_input[i][j])

    def connect_south(i,j):
        if(val_ind(i+1, j) and puzzle_input[i+1][j].tile in ('|', 'L', 'J', 'S')):
            puzzle_input[i+1][j].connected_to.append(puzzle_input[i][j])

    def connect_west(i,j):
        if(val_ind(i, j-1) and puzzle_input[i][j-1].tile in ('-', 'L', 'F', 'S')):
            puzzle_input[i][j-1].connected_to.append(puzzle_input[i][j])

    def connect_east(i,j):
        if(val_ind(i, j+1) and puzzle_input[i][j+1].tile in ('-', 'J', '7', 'S')):
            puzzle_input[i][j+1].connected_to.append(puzzle_input[i][j])
        
    puzzle_input = list(map(list, open("input/10.txt").read().splitlines()))
    start = ()
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            puzzle_input[i][j] = Node(puzzle_input[i][j], i, j)
    
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            match puzzle_input[i][j].tile:
                case '|': #is a vertical pipe connecting north and south.
                    connect_north(i,j)
                    connect_south(i,j)
                case '-':#is a horizontal pipe connecting east and west.
                    connect_east(i,j)
                    connect_west(i,j)
                case 'L': # is a 90-degree bend connecting north and east.
                    connect_north(i,j)
                    connect_east(i,j)
                case 'J': # is a 90-degree bend connecting north and west.
                    connect_north(i,j)
                    connect_west(i,j)
                case '7': # is a 90-degree bend connecting south and west.
                    connect_south(i,j)
                    connect_west(i,j)
                case 'F': # is a 90-degree bend connecting south and east.
                    connect_south(i,j)
                    connect_east(i,j)
                case 'S':
                    start = puzzle_input[i][j]
                #. is ground; there is no pipe in this tile.

    print(part1(start))
    print(part2(start, puzzle_input, start))
