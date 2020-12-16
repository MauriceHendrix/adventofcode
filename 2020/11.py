import copy
seat_rows = list(map(list, open('input-11.txt').read().split('\n')))


def count_occupied(seat_rows):
    count =0;
    for row in seat_rows:
        for seat in row:
            count += seat == '#'
    return count

def count_adjacent(i, j, seat_rows):
    count = 0
    # left
    if j > 0:
        count += seat_rows[i][j-1] == '#'
    # right
    if j < len(seat_rows[i]) - 1:
        count += seat_rows[i][j+1] == '#'
    # up
    if i > 0:
        count += seat_rows[i-1][j] == '#'
    #down
    if i < len(seat_rows) -1:
        count += seat_rows[i+1][j] == '#'
    # left up diagonal
    if j > 0 and i > 0:
        count += seat_rows[i-1][j-1] == '#'
    # right up diagonal
    if j < len(seat_rows[i]) - 1 and i > 0:
        count += seat_rows[i-1][j+1] == '#'
    # left down diagonal
    if j > 0 and i < len(seat_rows) -1:
        count += seat_rows[i+1][j-1] == '#'
    # right down diagonal
    if j < len(seat_rows[i]) - 1 and i < len(seat_rows) -1:
        count += seat_rows[i+1][j+1] == '#'
    return count

def seat_change(seat_rows, count_adjacent_func, occupied_threshold):

    seat_rows_changed = copy.deepcopy(seat_rows)
    for i, seat_row in enumerate(seat_rows):
        for j, seat in enumerate(seat_row):
            num_adjacent = count_adjacent_func(i,j, seat_rows)
            if num_adjacent == 0 and seat == 'L':
                seat_rows_changed[i][j] = '#'
            if num_adjacent >= occupied_threshold and seat == '#':
                seat_rows_changed[i][j] = 'L'
    return seat_rows_changed

def count_adjacent2(i, j, seat_rows):
    count = 0
    # left
    k, l = i,j
    while l > 0 and seat_rows[k][l-1] == '.':
        l -=1
    if l > 0:
        count += seat_rows[k][l-1] == '#'

    # right
    k, l = i,j
    while l < len(seat_rows[i]) - 1 and seat_rows[k][l+1] == '.':
        l += 1
    if l < len(seat_rows[k]) - 1:
        count += seat_rows[k][l+1] == '#'

    # up
    k, l = i, j
    while k > 0 and seat_rows[k-1][l] == '.':
        k -= 1
    if k > 0:
        count += seat_rows[k-1][l] == '#'
    
    #down
    k, l = i, j
    while k < len(seat_rows) -1 and seat_rows[k+1][l] == '.':
        k += 1
    if k < len(seat_rows) -1:
        count += seat_rows[k+1][l] == '#'
    
    # left up diagonal
    k, l = i,j
    while k > 0 and l > 0 and seat_rows[k-1][l-1] == '.':
        k, l = k-1, l - 1
    if l > 0 and k > 0:
        count += seat_rows[k-1][l-1] == '#'

    # right up diagonal
    k, l = i, j
    while k > 0 and l < len(seat_rows[i]) - 1 and seat_rows[k-1][l+1] == '.':
        k, l = k-1, l + 1
    if l < len(seat_rows[k]) - 1 and k > 0:
        count += seat_rows[k-1][l+1] == '#'
    
    # left down diagonal
    k, l = i,j
    while k < len(seat_rows) -1  and l > 0 and seat_rows[k+1][l-1] == '.':
        k, l = k+1, l - 1
    if l > 0 and k < len(seat_rows) -1:
        count += seat_rows[k+1][l-1] == '#'

    # right down diagonal
    k, l = i,j
    while k < len(seat_rows) -1  and l < len(seat_rows[i]) - 1 and seat_rows[k+1][l+1] == '.':
        k, l = k+1, l + 1
    if l < len(seat_rows[k]) - 1 and k < len(seat_rows) -1:
        count += seat_rows[k+1][l+1] == '#'

    return count

def find_stable_config(count_adjacent_func, occupied_threshold):
    current_seat_rows = seat_rows
    change_rows = seat_change(current_seat_rows, count_adjacent_func, occupied_threshold=5)
    while change_rows != current_seat_rows:
        current_seat_rows = change_rows
        change_rows = seat_change(current_seat_rows, count_adjacent_func, occupied_threshold=5)
    return count_occupied(current_seat_rows)

print(find_stable_config(count_adjacent, occupied_threshold=4))
print(find_stable_config(count_adjacent2, occupied_threshold=5))
