def tilt(platform):
    for j in range(len(platform[0])):
        available_spots = []
        for i in range(len(platform)):
            if(platform[i][j]=='.'):
                available_spots.insert(0, i)
            elif(platform[i][j]=='#'):
                available_spots = []
            elif(len(available_spots) != 0):
                move_to = available_spots.pop()
                platform[move_to][j]='O'
                platform[i][j]='.'
                available_spots.insert(0, i)
    return platform

if __name__ == "__main__":
    puzzle_input = list(map(list, open("input/14.txt").read().splitlines()))
    platform = tilt(puzzle_input)
    print()
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            print(platform[i][j], end='')
        print()
    print(sum((platform[i].count('O') * (len(platform)-i)  for i in range(len(platform)))))