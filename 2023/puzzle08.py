from itertools import cycle
from math import lcm

def part1(instructions, nav_nodes):
    steps = 0
    node = nav_nodes['AAA']
    for instr in cycle(instructions):
        steps += 1
        next_key = node[0 if instr == 'L' else 1]
        node = nav_nodes[node[0 if instr == 'L' else 1]]
        if next_key == 'ZZZ':
            break
    return steps


def calc_steps(start_node, instructions, nav_nodes):
    steps = 0
    node = start_node
    for instr in cycle(instructions):
        steps += 1
        next_key = node[0 if instr == 'L' else 1]
        node = nav_nodes[node[0 if instr == 'L' else 1]]
        if next_key.endswith('Z'):
            break
    return steps

def part2(instructions, nav_nodes):
    steps = 0
    nodes = [n for k, n in nav_nodes.items() if k.endswith('A')]
    steps_calc= [calc_steps(sn, instructions, nav_nodes) for sn in nodes]
    return lcm(*steps_calc)

    


if __name__ == "__main__":
    puzzle_input = open("input/08.txt").read().splitlines()
    instructions = puzzle_input[0]
    nav_nodes = {}    
    for direction in puzzle_input[2:]:
        key, left, right = direction[:3], direction[7:10], direction[12:15]
        nav_nodes[key] = (left, right)
    print(part1(instructions, nav_nodes))
    print(part2(instructions, nav_nodes))
