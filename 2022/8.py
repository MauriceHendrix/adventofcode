from dataclasses import dataclass
from typing import List
input = open('8.txt').readlines()

grid = []
visible = []
#row_max_ltr = []
#row_max_rtl = []
#col_max_ttb = []
#col_max_btt = []

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


for i in range(len(grid)):
    for j in range(len(grid[-1])):
        row_max_ltr[i][j] = grid[i][j]
        row_max_rtl[i][-j-1] = grid[i][-j-1]
        col_max_ttb[i][j] = grid[i][j]
        col_max_btt[-i-1][j] = grid[-i-1][j]
        if j > 0:
            row_max_ltr[i][j] = max(grid[i][j], row_max_ltr[i][j-1])
            row_max_rtl[i][-j-1] = max(grid[i][-j-1], row_max_rtl[i][-j])
        if i > 0:
            col_max_ttb[i][j] = max(grid[i][j], col_max_ttb[i-1][j])
            col_max_btt[-i-1][j] = max(grid[-i-1][j], col_max_btt[-i][j])
    
for i in range(1, len(grid) -1):
    for j in range(1, len(grid[i])-1):
        #ltr
        if row_max_ltr[i][j-1] < grid[i][j]:
            visible[i][j] = 1
        #rtl
        if row_max_rtl[i][j+1] < grid[i][j]:
            visible[i][j] = 1
        #ttb
        if col_max_ttb[i-1][j] < grid[i][j]:
            visible[i][j] = 1
        #btt
        if col_max_btt[i+1][j] < grid[i][j]:
            visible[i][j] = 1

#print(grid)
#print(row_max_ltr)
#print(row_max_rtl)
#print(col_max_ttb)
#print(col_max_btt)
#print(visible)
print(sum(sum(lst) for lst in visible))