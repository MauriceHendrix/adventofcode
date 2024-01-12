import sys

def get_neighbours(start, grid, path, distance, min_stretch, max_strecht):
    def add_next(direction, i_func, j_func, i, j, dist):
        neighbours = []
        npath = path
        curr_dist, ni, nj = dist, i, j
        while npath != direction * max_strecht:
            npath = (npath + direction)[-max_strecht:]
            ni = i_func(ni)
            nj = j_func(nj)
            if ni < 0 or  nj < 0 or ni >= len(grid) or nj >= len(grid[0]):
                break
            curr_dist += grid[ni][nj]
            if min_stretch == 0 or npath[-min_stretch:] == direction * min_stretch:
                neighbours.append(((ni, nj), npath, curr_dist))
        return neighbours

    i,j = start
    dist = distance[i][j][path]
    neighbours = []
    if path[-1:] in ('>', '<', ''):
        neighbours.extend(add_next('^', lambda ni: ni-1, lambda nj: nj, i, j, dist))
        neighbours.extend(add_next('V', lambda ni: ni+1, lambda nj: nj, i, j, dist))
    if path[-1:] in ('^', 'V', ''):
        neighbours.extend(add_next('<', lambda ni: ni, lambda nj: nj-1, i, j, dist))
        neighbours.extend(add_next('>', lambda ni: ni, lambda nj: nj+1, i, j, dist))
    return neighbours

def least_cost(grid, min_stretch, max_strecht):
    distance = [[{} for _ in range(len(grid[0]))] for __ in grid]
    distance[0][0][''] = 0
    Q = set()
    Q.add(((0,0), ''))
    upper_bound = (len(grid[0]) + len(grid))*9
    while Q:
        (i, j), path = Q.pop()
        dist = distance[i][j][path]
        for (ni, nj), npath, curr_dist in get_neighbours((i,j), grid, path, distance, min_stretch, max_strecht):
            old_dist = distance[ni][nj].get(npath, sys.maxsize)
            if curr_dist < old_dist and curr_dist <= upper_bound:
                distance[ni][nj][npath] = curr_dist
                Q.add(((ni, nj), npath))
    return min(distance[len(puzzle_input)-1][len(puzzle_input[0])-1].values())

if __name__ == "__main__":
    puzzle_input = [[int(ch) for ch in ln] for ln in open("input/17.txt").read().strip().split('\n')]
    print(least_cost(puzzle_input, 0, 3))
    print(least_cost(puzzle_input, 4, 10))
