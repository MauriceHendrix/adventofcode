input = open('2.txt').readlines()

move_score = {'rock': 1, 'paper': 2, 'scissors': 3}
rpc_lookup = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
defeats_lookup = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
defeated_by_lookup = {v: k for k, v in defeats_lookup.items()}

total_score = 0
for line in input:
    total_score += move_score[rpc_lookup[line[2]]]
    if rpc_lookup[line[0]] == rpc_lookup[line[2]]: # draw
        total_score += 3
    elif defeats_lookup[rpc_lookup[line[2]]] == rpc_lookup[line[0]]:
        total_score += 6
    
print(total_score)

total_score = 0
for line in input:
    opponent = rpc_lookup[line[0]]
    if line[2] == 'X': # means you need to lose
        me = defeats_lookup[opponent]
        total_score += move_score[me]
    elif line[2] == 'Y':  # means you need to end the round in a draw
        total_score += move_score[rpc_lookup[line[0]]]
        total_score += 3
    elif line[2] == 'Z': # means you need to win. Good luck!
        me = defeated_by_lookup[opponent]
        total_score += move_score[me]
        total_score += 6

print(total_score)