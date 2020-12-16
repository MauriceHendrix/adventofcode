boarding_cards = open('input-6.txt').readlines()
boarding_cards.append('\n')

groups = []
group = set()
for line in boarding_cards:
    if line == '\n': 
        groups.append(group)
        group = set()
    else:
        group.update(set(line.rstrip()))

print("sum for questions where anyone entered yes:")
print(sum(map(len, groups)))



groups = []
group = None
for line in boarding_cards:
    if line == '\n':
        groups.append(set() if group is None else group)
        group = None
    else:
        group = set(line.rstrip()) if group is None else group.intersection(set(line.rstrip()))


print("sum for questions where everyone entered yes:")
print(sum(map(len, groups)))