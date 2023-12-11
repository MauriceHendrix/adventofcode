class Node:
    def __init__(self, tile, i, j):
        self.tile, self.i, self.j, self.connected_to = tile, i, j, []

    def __repr__(self):
        return f'({self.i},{self.j}:{self.tile})'
    

def part1(puzzle_input, adj_mattr):
    return ''

def part2(puzzle_input, adj_mattr):
    return ''

if __name__ == "__main__":
    def val_ind(i, j):
        return 0 <= i < len(puzzle_input) and 0 <= j < len(puzzle_input[i])
        
    def connect_north(i,j):
        if(val_ind(i-1, j)):
            puzzle_input[i-1][j].connected_to.append(puzzle_input[i][j])
            puzzle_input[i][j].connected_to.append(puzzle_input[i-1][j])

    def connect_south(i,j):
        if(val_ind(i-1, j)):
            puzzle_input[i-1][j].connected_to.append(puzzle_input[i][j])
            puzzle_input[i][j].connected_to.append(puzzle_input[i-1][j])

    def connect_east(i,j):
        if(val_ind(i, j-1)):
            puzzle_input[i][j-1].connected_to.append(puzzle_input[i][j])
            puzzle_input[i][j].connected_to.append(puzzle_input[i][j-1])

    def connect_west(i,j):
        if(val_ind(i, j+1)):
            puzzle_input[i][j+1].connected_to.append(puzzle_input[i][j])
            puzzle_input[i][j].connected_to.append(puzzle_input[i][j+1])
        
    puzzle_input = list(map(list, open("input/10.txt").read().splitlines()))
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            puzzle_input[i][j] = Node(puzzle_input[i][j], i, j)
    #print(puzzle_input)
    
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            match puzzle_input[i][j].tile:
                case '|': #is a vertical pipe connecting north and south.
                    connect_north(i,j)
                    connect_south(i,j)
                case '-':#is a horizontal pipe connecting east and west.
                    connect_east(i,j)
                    connect_west(i,j)
                case 'L':
                    pass # is a 90-degree bend connecting north and east.
                case 'J':
                    pass # is a 90-degree bend connecting north and west.
                case '7':
                    pass # is a 90-degree bend connecting south and west.
                case 'F':
                    pass # is a 90-degree bend connecting south and east.
                case 'S':
                    start = (i, j)
                #. is ground; there is no pipe in this tile.
            print(puzzle_input[i][j].tile, end='')
        print()

    #print(adj_mat)
#    print(part1(adj_mattr))
#    print(part2(adj_mattr))
