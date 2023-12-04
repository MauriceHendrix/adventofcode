import re
from utility.timing import timing

def is_symbol(char):
    return not char.isdigit() and char != '.' # and char != '\n'

def part1(puzzle_input: list[str]):
    total_score = 0
    for card in puzzle_input:
        score = 0
        card = card.replace('  ', ' ')
        card = re.sub(r'Card.*[0-9]+:', '', card)
        card = card.split('|')
        card[0] = list(map(int, card[0].strip().split(' ')))
        card[1] = list(map(int, card[1].strip().split(' ')))
        for num in card[0]:
            if(num in card[1]):
                score = max(1, score * 2)
        total_score += score
    return total_score

@timing
def part2(puzzle_input: list[str]):
    cards = {}
    for card in puzzle_input:
        score = 0
        card = card.replace('  ', ' ')
        card_num = int(re.match('Card *([0-9]+):', card).group(1))
        card = re.sub(r'Card.*[0-9]+:', '', card)
        card = card.split('|')
        card[0] = list(map(int, card[0].strip().split(' ')))
        card[1] = list(map(int, card[1].strip().split(' ')))
        cards[card_num] = [card]
    card_num = 1
    while card_num < len(puzzle_input):
        count = 0
        for num in cards[card_num][0][0]:
            if(num in cards[card_num][0][1]):
                count += 1
        for _ in cards[card_num]:
            for i in range(card_num+1, card_num+1+count):
                if i <= len(puzzle_input):
                    cards[i].append([])
        card_num += 1
    total_count = 0
    for crd in cards.values():
        total_count += len(crd)
    return total_count

@timing
def part2b(puzzle_input: list[str]):
    cards = {}
    cards_dup = {}
    for card in puzzle_input:
        score = 0
        card = card.replace('  ', ' ')
        card_num = int(re.match('Card *([0-9]+):', card).group(1))
        card = re.sub(r'Card.*[0-9]+:', '', card)
        card = card.split('|')
        card[0] = list(map(int, card[0].strip().split(' ')))
        card[1] = list(map(int, card[1].strip().split(' ')))
        cards[card_num] = [card]
        cards_dup[card_num] = 1
    card_num = 1
    while card_num < len(puzzle_input):
        count = 0
        exists = {}
        for num in cards[card_num][0][0]:
            exists[num]=0
        for num in cards[card_num][0][1]:
            exists[num] = exists.get(num,-1)+1
        count = sum(exists.values())
        for _ in range(cards_dup[card_num]):
            for i in range(card_num+1, card_num+1+count):
                if i <= len(puzzle_input):
                    cards_dup[i] += 1
        card_num += 1
    return sum(cards_dup.values())

@timing
def part2c(puzzle_input: list[str]):
    cards = []
    cards_dup = []
    for card in puzzle_input:
        score = 0
        card = card.replace('  ', ' ')
        card_num = int(re.match('Card *([0-9]+):', card).group(1))
        card = re.sub(r'Card.*[0-9]+:', '', card)
        card = card.split('|')
        card[0] = list(map(int, card[0].strip().split(' ')))
        card[1] = list(map(int, card[1].strip().split(' ')))
        cards.append([card])
        cards_dup.append(1)
    card_num = 1
    while card_num < len(puzzle_input):
        count = 0
        exists = {}
        for num in cards[card_num-1][0][0]:
            exists[num]=0
        for num in cards[card_num-1][0][1]:
            exists[num] = exists.get(num,-1)+1
        count = sum(exists.values())
        for _ in range(cards_dup[card_num-1]):
            for i in range(card_num+1, card_num+1+count):
                if i <= len(puzzle_input):
                    cards_dup[i-1] += 1
        card_num += 1
    return sum(cards_dup)

@timing
def part2d(puzzle_input: list[str]):
    cards = []
    cards_dup = []
    for card in puzzle_input:
        score = 0
        card = card.replace('  ', ' ')
        card_num = int(re.match('Card *([0-9]+):', card).group(1))
        card = re.sub(r'Card.*[0-9]+:', '', card)
        card = card.split('|')
        card[0] = sorted(list(map(int, card[0].strip().split(' '))))
        card[1] = sorted(list(map(int, card[1].strip().split(' '))))
        cards.append([card])
        cards_dup.append(1)
    card_num = 1
    while card_num < len(puzzle_input):
        count = 0
        exists = {}
        i = 0
        while i < len(cards[card_num-1][0][0]):
            j = 0
            while j < len(cards[card_num-1][0][1]) and i < len(cards[card_num-1][0][0]):
                if(cards[card_num-1][0][0][i] == cards[card_num-1][0][1][j]):
                    count += 1
                    i, j = i+1, j+1
                elif(cards[card_num-1][0][0][i] < cards[card_num-1][0][1][j]):
                    i += 1
                elif(cards[card_num-1][0][0][i] > cards[card_num-1][0][1][j]):
                    j += 1
            i += 1
        
        for _ in range(cards_dup[card_num-1]):
            i = 0
            while i < count:
                if i+card_num <= len(puzzle_input):
                    cards_dup[i+card_num] += 1
                i += 1
        card_num += 1
    return sum(cards_dup)

if __name__ == "__main__":
    puzzle_input = open("input/04.txt").read().splitlines() 
    print(part1(puzzle_input))
    print(part2(puzzle_input))
    print(part2b(puzzle_input))
    print(part2c(puzzle_input))
    print(part2d(puzzle_input))
