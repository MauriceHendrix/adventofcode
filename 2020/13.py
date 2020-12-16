from functools import reduce
from math import ceil

puzzle_input = open('input-13.txt').readlines()

earliest_departure = int(puzzle_input[0])
timetable_with_out_of_service = puzzle_input[1].split(',')
timetable = [int(t) for t in timetable_with_out_of_service if t!='x']

waiting_times = [(ceil(earliest_departure / t)*t - earliest_departure, t) for t in timetable]
first_bus = min(waiting_times)
print('bus * waiting:')
print(first_bus[0]*first_bus[1])

departure_busses = []
for i, b in enumerate(timetable_with_out_of_service):
    if b != 'x':
        departure_busses.append((int(b), int(b)-i))

print(timetable_with_out_of_service)
print(departure_busses)
#print([i-b  for i,b in departure_busses])
#print(lcm(*[i-b  for i,b in departure_busses]))

# Python Program to find the L.C.M. of two input number

def chinese_remainder(departure_busses):
    def inverse(a,b):
        return pow(a, -1, b)
    bi = [n[1] for n in departure_busses] # remainders
    N = reduce((lambda x, y: x * y), [n[0] for n in departure_busses]) # multiplication of mod numbers
    Ni = [int(N/n[0]) for n in departure_busses] # N / current mod number
    xi = [inverse(Ni[i], dep[0]) for i, dep in enumerate(departure_busses)]
    products = [t[0]*t[1]*t[2]for t in zip(bi,Ni,xi)]
    sum_of_products = sum(products)
    return sum_of_products % N

inputs = [(int(x), int(x) - p) for p, x in enumerate(puzzle_input[1].split(",")) if x != "x"]
print(inputs)
print("CRT", chinese_remainder(inputs))