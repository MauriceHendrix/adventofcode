import copy

def tilt(platform, ew_range, ns_range, i_j_func, move_func):
    for i in ew_range:
        available_spots = []
        for j in ns_range:
            if(platform[i_j_func(i,j)[0]][i_j_func(i,j)[1]]=='.'):
                available_spots.insert(0, j)
            elif(platform[i_j_func(i,j)[0]][i_j_func(i,j)[1]]=='#'):
                available_spots = []
            elif(len(available_spots) != 0):
                move_to = available_spots.pop()
                platform[move_func(i,j, move_to)[0]][move_func(i,j, move_to)[1]]='O'
                platform[i_j_func(i,j)[0]][i_j_func(i,j)[1]]='.'
                available_spots.insert(0, j)
    return platform
    
def tilt_east(platform):
    for i in range(len(platform)):
        available_spots = []
        for j in range(len(platform[i])):
            if(platform[i][j]=='.'):
                available_spots.insert(0, j)
            elif(platform[i][j]=='#'):
                available_spots = []
            elif(len(available_spots) != 0):
                move_to = available_spots.pop()
                platform[i][move_to]='O'
                platform[i][j]='.'
                available_spots.insert(0, j)
    return platform

def cycle(platform):
    platform = tilt(platform, range(len(platform[0])), range(len(platform)), lambda i,j: (j, i), lambda i,j,m: (m, i))  # tilt north
    platform = tilt(platform, range(len(platform)), range(len(platform[0])), lambda i,j: (i, j), lambda i,j,m: (i, m))  # tilt west
    platform = tilt(platform, range(len(platform[0])), range(len(platform)-1, -1, -1), lambda i,j: (j, i), lambda i,j,m: (m, i))  # tilt south
    platform = tilt(platform, range(len(platform)), range(len(platform[0])-1, -1, -1), lambda i,j: (i, j), lambda i,j,m: (i, m))  # tilt east
    return platform


def print_platform(platform):
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            print(platform[i][j], end='')
        print()

def part1():
    platform = list(map(list, open("input/14.txt").read().splitlines()))
    platform = tilt(platform, range(len(platform[0])), range(len(platform)), lambda i,j: (j, i), lambda i,j,m: (m, i))  # tilt north
    return sum((platform[i].count('O') * (len(platform)-i)  for i in range(len(platform))))

def part2(cycles):
    platform = list(map(list, open("input/14.txt").read().splitlines()))
    maps = {}
    prev_index = {}
    i=1
    while i<= cycles:
        playform_key = str(platform)
        if playform_key in maps:
            platform = copy.deepcopy(maps[playform_key])
        else:
            platform = cycle(platform)
            maps[playform_key] = copy.deepcopy(platform)

        pref_key = str(platform)
        if pref_key not in prev_index:
            prev_index[pref_key] = i
        else:
            cycle_length = i-prev_index[pref_key]
            rest = cycles-i
            full_cycles = rest // cycle_length
            i += (full_cycles * cycle_length)
            prev_index = {}
        i+=1
    return sum((platform[i].count('O') * (len(platform)-i)  for i in range(len(platform))))

if __name__ == "__main__":
    print(part1())
    print()
    print(part2(1000000000))
