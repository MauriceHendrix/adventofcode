import re

games = {}
colours = ("blue", "red", "green")

def get_game_num(game):
        game_num = re.findall("Game.*: ", game )
        game = game.replace(game_num[0] , "")
        return int(game_num[0].replace("Game ", "").replace(": ", "")), game_num[0]

def set_colour(game_num, game, colour):
        colour_num = re.findall("[0-9]* " + colour, game)
        for match in colour_num:
            count = int(match.replace(colour, "").strip())
            games.setdefault(game_num, {})
            games[game_num].setdefault(colour, [])
            games[game_num][colour].append(count)


def part1(puzzle_input: list[str], restrictions):
    count = 0
    for game in puzzle_input:
        allowed = True
        game_num, game_num_str = get_game_num(game)
        game = game.replace(game_num_str, "")
        for col in colours:
            set_colour(game_num , game, col)
            for cnt in games[game_num][col]:
                allowed = allowed and cnt <= restrictions[col]
        if allowed:
            count += game_num 
    return(count)


def part2(puzzle_input: list[str], restrictions):
    count = 0
    power_sum = 0
    for game in puzzle_input:
        allowed = True
        game_num, game_num_str = get_game_num(game)
        game = game.replace(game_num_str, "")
        power = 1
        for col in colours:
            set_colour(game_num , game, col)
            power = power * max(games[game_num][col])
        power_sum += power
    return(power_sum)


if __name__ == "__main__":
    puzzle_input = open("input/02.txt").readlines()
    print(part1(puzzle_input, {'red': 12, 'green': 13, 'blue': 14}))
    print(part2(puzzle_input, {'red': 12, 'green': 13, 'blue': 14}))
