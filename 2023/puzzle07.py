card_rank = {'A': '14', 
             'K': '13',
             'Q': '12',
             'J': '11',
             'T': '10',
             '9': '09',
             '8': '08',
             '7': '07',
             '6': '06',
             '5': '05',
             '4': '04',
             '3': '03',
             '2': '02',
             'J': '01' }
             
def of_a_kind(card, matches):
    return any(len(card.replace(card[i], '')) == len(card) - matches for i in range(len(card)))

def cards_rank(card_bid):
    card = card_bid[0]
    rank_str = ''
    # get type
    if(of_a_kind(card, 5)): # 5 of a kind
        rank_str += '6'
    elif(of_a_kind(card, 4)): # 4 of a kind
        rank_str += '5'
    elif(of_a_kind(card, 3)): # 3 of a kind
        if(of_a_kind(card, 2)): # full house
            rank_str += '4'
        else:
            rank_str += '3'
    elif(of_a_kind(card, 2)): # 2 of a kind
        i, sorted_card = 0, "".join(sorted(card))
        while i < len(sorted_card):
            if(i < len(sorted_card)-1 and sorted_card[i] == sorted_card[i+1]):
                break
            i+=1
        if (of_a_kind(sorted_card[i+1:], 2)): # 2 pair
            rank_str += '2'
        else: # 1 pair
            rank_str += '1'
    else:
        rank_str += '0'

    for crd in card:
        rank_str += card_rank[crd]

    return(int(rank_str))
    
    
def cards_rank2(card_bid):
    card = card_bid[0]
    rank_str = ''
    type_rank = 0
    vier, cahr = False, ''
    # get type
    for crd in card_rank.keys():
        if crd != 'J':
            if(card.count(crd) + card.count('J') == 5): # 5 of a kind
                type_rank = 6
                break
            elif(card.count(crd) + card.count('J') == 4): # 4 of a kind
                type_rank = max(type_rank, 5)

            elif(card.count(crd) + card.count('J') == 3): # 3 of a kind
                check_card = card.replace(crd, '').replace('J', '')
                if(of_a_kind(check_card, 2)): # full house
                    type_rank = max(type_rank, 4)
                else:
                    type_rank = max(type_rank, 3)
            elif(card.count(crd) + card.count('J') == 2): # 2 of a kind
                check_card = card.replace(crd, '').replace('J', '')
                if(of_a_kind(check_card, 2)): # 2 pair
                    type_rank = max(type_rank, 2)
                else:
                    type_rank = max(type_rank, 1)

    rank_str += str(type_rank)
    for crd in card:
        rank_str += card_rank[crd]

    return(int(rank_str))

def part1(cards_and_bids):
    cards_and_bids.sort(key=cards_rank, reverse=True)
    score_count = 0
    for i, card_bid in enumerate(cards_and_bids):
        score_count += (len(cards_and_bids) -i) * card_bid[1]
    return score_count

def part2(cards_and_bids):
    cards_and_bids.sort(key=cards_rank2, reverse=True)
    score_count = 0
    for i, card_bid in enumerate(cards_and_bids):
        score_count += (len(cards_and_bids) -i) * card_bid[1]
    return score_count

if __name__ == "__main__":
    puzzle_input = open("input/07.txt").read().splitlines()
    cards_and_bids = []
    for card in puzzle_input:
        card, bid = card.split()
        cards_and_bids.append((card, int(bid)))
    print(part1(cards_and_bids))
    print(part2(cards_and_bids))
