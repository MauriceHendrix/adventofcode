import string
input = open('5.txt').readlines()


# read in stacks
stacks = []
for line in input:
    for i in range(0, len(line), 4):
        stack_index = (i+4) // 4 - 1
        if len(stacks) < stack_index + 1:
            stacks.append([])
        if line[i] == '[':
            stacks[stack_index].append(line[i+1:i+2])
            #print(line[i+1:i+2])
    if '[' not in line:
        break

def move(num, frm, to):
    for _ in range(num):
        item = stacks[frm-1].pop(0)
        stacks[to-1].insert(0, item)

for line in input:
    if not line.startswith('move'):
        continue
    args = map(int, line.strip().replace('move ', '').replace('from ', '').replace('to ', '').split(' '))
    move(*args)
    

top = ''
for stack in stacks:
    top += stack[0]

print(top)

## part 2

# read in stacks
stacks = []
for line in input:
    for i in range(0, len(line), 4):
        stack_index = (i+4) // 4 - 1
        if len(stacks) < stack_index + 1:
            stacks.append([])
        if line[i] == '[':
            stacks[stack_index].append(line[i+1:i+2])
            #print(line[i+1:i+2])
    if '[' not in line:
        break

def move_pt2(num, frm, to):
    stacks[to-1] = stacks[frm-1][:num] + stacks[to-1]
    del stacks[frm-1][:num]

for line in input:
    if not line.startswith('move'):
        continue
    args = map(int, line.strip().replace('move ', '').replace('from ', '').replace('to ', '').split(' '))
    move_pt2(*args)
    

top = ''
for stack in stacks:
    top += stack[0]
print(top)