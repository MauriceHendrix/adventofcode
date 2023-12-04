import re

def is_symbol(char):
    return not char.isdigit() and char != '.' # and char != '\n'

def part1(puzzle_input: list[str]):
    total = 0
    for i in range(len(puzzle_input)):
        num_str = ''
        puzzle_input[i] += '.'  # don't want to deal with end of line differently, so added an extra .
        for j in range(len(puzzle_input[i])):
            if (puzzle_input[i][j].isdigit()):
                num_str += puzzle_input[i][j]
            else:
                if j > 0 and puzzle_input[i][j-1].isdigit():
                    # right, left, top, bottom, diagonal top right, diagonal top left, diagonal bottom right, diagonal bottom left
                    if is_symbol(puzzle_input[i][j]):
                        total += int(num_str)
                    elif j - len(num_str) > 0 and is_symbol(puzzle_input[i][j - 1 - len(num_str)]):
                        total += int(num_str)
                    elif i > 0 and any(map(is_symbol, puzzle_input[i-1][max(0, j - 1 - len(num_str)): min(len(puzzle_input[i]), j+1)])):
                        total += int(num_str)
                    elif i+1 < len(puzzle_input) -1 and any(map(is_symbol, puzzle_input[i+1][max(0, j - 1 - len(num_str)): min(len(puzzle_input[i]) -1 , j+1)])):
                        total += int(num_str)
                num_str = ''
    return total


def part2(puzzle_input: list[str]):
    total = 0
    for i in range(len(puzzle_input)):
        puzzle_input[i] += '.'  # don't want to deal with end of line differently, so added an extra .
        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] == '*':
                found_nums = []
                # num to right
                r = j+1
                if(puzzle_input[i][r].isdigit()):
                    while r < len(puzzle_input[i]) -1 and puzzle_input[i][r].isdigit():
                        r += 1
                    found_nums += [int(puzzle_input[i][j+1 : r])]
                    print(found_nums)
                l = j-1
                # num to left
                if(l > 0 and puzzle_input[i][l].isdigit()):
                    while(l >= 0 and puzzle_input[i][l].isdigit()):
                        l-= 1
                    found_nums += [int(puzzle_input[i][l+1 : j])]
                # num on top
                if(i > 0):
                    l, r = max(0, j-1), j+1
                    while l > 0 and (puzzle_input[i-1][l].isdigit()):
                        l-=1
                    while (puzzle_input[i-1][r].isdigit()):
                        r+=1
                    top_nums = re.findall('[0-9]+', puzzle_input[i-1][l:r])
                    found_nums += list(map(int, top_nums))
                # num at bottom
                if(i < len(puzzle_input) - 1):
                    l, r = max(0, j-1), j+1
                    while l > 0 and (puzzle_input[i+1][l].isdigit()):
                        l-=1
                    while (puzzle_input[i+1][r].isdigit()):
                        r+=1
                    top_nums = re.findall('[0-9]+', puzzle_input[i+1][l:r])
                    found_nums += list(map(int, top_nums))
                # num at bottom
                if len(found_nums) == 2:
                    total += (found_nums[0] * found_nums[1])
    return total


if __name__ == "__main__":
    puzzle_input = open("input/03.txt").read().splitlines() 
    print(part1(puzzle_input))
    print(part2(puzzle_input))
