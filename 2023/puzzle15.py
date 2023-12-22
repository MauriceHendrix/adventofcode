stored_hashes = {}
def hash_func(chars, multiplier):
    if chars in stored_hashes:
        return stored_hashes[chars]
    curr = 0
    for char in chars:
        curr += ord(char)
        curr *= multiplier
        curr = curr % 256
    stored_hashes[chars] = curr
    return curr
    
def part1(lst_seq, multiplier):
    return(sum(hash_func(seq, multiplier) for seq in lst_seq))

if __name__ == "__main__":
    puzzle_input = open("input/15.txt").read().replace('\n', '').split(',')
    chars = 'cm-'
#    print(hash_func(chars, 17))
    print(part1(puzzle_input, 17))
