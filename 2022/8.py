from dataclasses import dataclass
from typing import List
input = open('8.txt').readlines()

grid = []
visible = []

for line in input:
    line = line.strip()
    grid.append(list(map(int, list(line))))

    visible.append([0]*len(line))
    visible[-1][0] = 1
    visible[-1][-1] = 1

row_max_ltr = [[0 for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
row_max_rtl = [[0 for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
col_max_ttb = [[0 for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
col_max_btt = [[0 for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
visible[0] = [1] * len(visible[0])
visible[-1] = [1] * len(visible[0])

#part 1

for i in range(len(grid)):
    for j in range(len(grid[-1])):
        row_max_ltr[i][j] = grid[i][j]
        row_max_rtl[i][-j-1] = grid[i][-j-1]
        col_max_ttb[i][j] = grid[i][j]
        col_max_btt[-i-1][j] = grid[-i-1][j]
        if j > 0:
            #ltr
            row_max_ltr[i][j] = max(grid[i][j], row_max_ltr[i][j-1])
            if row_max_ltr[i][j-1] < grid[i][j]:
                visible[i][j] = 1
            #rtl
            if row_max_rtl[i][-j] < grid[i][-j-1]:
                visible[i][-j-1] = 1
            row_max_rtl[i][-j-1] = max(grid[i][-j-1], row_max_rtl[i][-j])
        if i > 0:
            #ttb
            col_max_ttb[i][j] = max(grid[i][j], col_max_ttb[i-1][j])
            if col_max_ttb[i-1][j] < grid[i][j]:
                visible[i][j] = 1
            #btt
            if col_max_btt[-i][j] < grid[-i-1][j]:
                visible[-i-1][j] = 1
            col_max_btt[-i-1][j] = max(grid[-i-1][j], col_max_btt[-i][j])


print(sum(sum(lst) for lst in visible))

# part2
row_trees_ltr = [[{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
row_trees_rtl = [[{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
col_trees_ttb = [[{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
col_trees_btt = [[{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} for _ in range(len(grid))] for _ in range(len(grid[-1])) ]
scenic_score = [[1 for _ in range(len(grid))] for _ in range(len(grid[-1])) ]

for i in range(len(grid)):
    for j in range(len(grid[-1])):
        for height in row_trees_ltr[i][j].keys():
            #ltr
            if j > 0: 
                if height > grid[i][j-1]:
                    row_trees_ltr[i][j][height] = row_trees_ltr[i][j-1][height] + 1
                else:
                    row_trees_ltr[i][j][height] = 1
            #rtl
            if j < len(grid[-1]) -1:
                if height > grid[i][-j-1]:
                    row_trees_rtl[i][-j-2][height] = row_trees_rtl[i][-j-1][height] + 1
                else:
                    row_trees_rtl[i][-j-2][height] = 1
            #ttb
            if i > 0:
                if height > grid[i][j-1]:
                    col_trees_ttb[i][j][height] = col_trees_ttb[i-1][j][height] + 1
                else:
                    col_trees_ttb[i][j][height] = 1
            #btt
            if i < len(grid) -1:
                if height > grid[-i-1][j]:
                    col_trees_btt[-i-2][j][height] = col_trees_btt[-i-1][j][height] + 1
                else:
                    col_trees_btt[-i-2][j][height] = 1
        scenic_score[i][j] *= row_trees_ltr[i][j][grid[i][j]]
        scenic_score[i][j] *= col_trees_ttb[i][j][grid[i][j]]
        scenic_score[i][-j-1] *= row_trees_rtl[i][-j-1][grid[i][-j-1]]
        scenic_score[-i-1][j] *= col_trees_btt[-i-1][j][grid[-i-1][j]]

print(max(max(lst) for lst in scenic_score))