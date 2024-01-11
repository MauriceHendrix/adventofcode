import sys

def get_neighbours(start, grid, path):
    i,j = start
    neighbours = []
    if path[-1:] != '>' and path != '<<<' and j > 0:
        neighbours.append(((i, j-1), (path + '<')[-3:]))
    if path[-1:] != '<' and path != '>>>' and j+1 < len(grid[0]):
        neighbours.append(((i, j+1), (path + '>')[-3:]))
    if path[-1:] != 'V' and path != '^^^' and i > 0:
        neighbours.append(((i-1, j), (path + '^')[-3:]))
    if path[-1:] != '^' and path != 'VVV' and i+1 < len(grid):
        neighbours.append(((i+1, j), (path + 'V')[-3:]))
    return neighbours

def least_cost(start, destination, grid):
    distance = [[{} for _ in range(len(grid[0]))] for __ in grid]
    distance[start[0]][start[1]][''] = 0
    Q = set()
    Q.add((start, ''))
    while Q:
        (i, j), path = Q.pop()
        dist = distance[i][j][path]
        for (ni, nj), npath in get_neighbours((i,j), grid, path):
            old_dist = distance[ni][nj].get(npath, sys.maxsize)
            curr_dist = dist + grid[ni][nj]
            if curr_dist < old_dist:
                distance[ni][nj][npath] = curr_dist
                Q.add(((ni, nj), npath))
    di, dj = destination
    return min(distance[di][dj].values())

if __name__ == "__main__":
    puzzle_input = [[int(ch) for ch in ln] for ln in open("input/17.txt").read().strip().split('\n')]
    print(least_cost((0,0), (len(puzzle_input[0])-1, len(puzzle_input)-1), puzzle_input))