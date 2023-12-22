stored_hashes = {}
def hash_func(chars):
    if chars in stored_hashes:
        return stored_hashes[chars]
    curr = 0
    for char in chars:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    stored_hashes[chars] = curr
    return curr
    
def part1(lst_seq):
    return(sum(hash_func(seq) for seq in lst_seq))


box_labels = [[] for _ in range(256)]
box_numbers = [[] for _ in range(256)]

def print_boxes():
    for i in range(len(box_labels)):
        assert len(box_labels[i]) == len(box_numbers[i])
        if len(box_labels[i]) != 0:
            print(f'Box {i}:', end='')
            for j in range(len(box_labels[i])):
                print(f' [{box_labels[i][j]} {box_numbers[i][j]}]', end='')
            print()
            
def part2(lst_seq):
    for seq in lst_seq:
        if('-' in seq):
            chars = seq[:-1]
            box_num = hash_func(chars)
            if chars in box_labels[box_num]:
                idx_to_remove = box_labels[box_num].index(chars)
                box_labels[box_num].pop(idx_to_remove)
                box_numbers[box_num].pop(idx_to_remove)
        else: # '='
            chars, lens = seq.split('=')
            box_num = hash_func(chars)
            if chars in box_labels[box_num]:
                box_numbers[box_num][box_labels[box_num].index(chars)] = int(lens)
            else:
                box_labels[box_num].append(chars)
                box_numbers[box_num].append(int(lens))

#    print_boxes()
    
    total = 0
    for bx_num, lenses in enumerate(box_numbers):
        if len(lenses) > 0:
            for slot, lens in enumerate(lenses):
                total += (bx_num+1) * (slot+1) * lens   
    return total


if __name__ == "__main__":
    puzzle_input = open("input/15.txt").read().strip().split(',')
    print(part1(puzzle_input))
    print(part2(puzzle_input))
