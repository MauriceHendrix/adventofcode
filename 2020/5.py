import math

def get_seat_id(seat):
    row_from = 0
    row_to = 127
    seat_from = 0
    seat_to = 7
    for c in seat.upper():
        if c == 'F':
            row_to = math.floor(((row_to - row_from) / 2) + row_from)
        if c == 'B':
            row_from = math.ceil((row_to - row_from) / 2 + row_from)
        if c == 'L':
            seat_to = math.floor(((seat_to - seat_from) / 2) + seat_from)
        if c == 'R':
            seat_from = math.ceil((seat_to - seat_from) / 2 + seat_from)
    
    assert row_from == row_to
    assert seat_from == seat_to
    #return (row_from, seat_from, row_from * 8 + seat_from)
    return row_from * 8 + seat_from


#seats = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
seats = open("input-5.txt", "r").readlines()

print('highest set number:')
print(max(map(get_seat_id, open("input-5.txt", "r").readlines())))

print('my seat:')
seat_numbers = sorted(map(get_seat_id, open("input-5.txt", "r").readlines()))
for i, s in enumerate(seat_numbers):
    if i< len(seat_numbers) -1 and seat_numbers[i+1] - s > 1:
        print(s+1)
