import portion 
import sys
from operator import itemgetter
from collections import deque
from utility.timing import timing

class RangeMap:
    def __init__(self):
        self.ranges = []

    def insert(self, range_tripple):
        self.ranges.append(tuple(map(int, range_tripple)))

    def sort(self):
        self.ranges.sort(key=itemgetter(1))
        
    def get(self, i):
        for rng in self.ranges:
            if i >= rng[1] and i < rng[1] + rng[2]:
                return rng[0] + (i - rng[1])
        return i

seeds = []
seed_to_soil = RangeMap()
soil_to_fertilizer = RangeMap()
fertilizer_to_water = RangeMap()
water_to_light = RangeMap()
light_to_temperature = RangeMap()
temperature_to_humidity = RangeMap()
humidity_to_location = RangeMap()
test_to_maps = {'seed-to-soil map:': seed_to_soil, 
                'soil-to-fertilizer map:': soil_to_fertilizer, 
                'fertilizer-to-water map:': fertilizer_to_water, 
                'water-to-light map:': water_to_light, 
                'light-to-temperature map:': light_to_temperature, 
                'temperature-to-humidity map:': temperature_to_humidity, 
                'humidity-to-location map:': humidity_to_location}

def read(input):
    map = None
    for line in input:
        if line in test_to_maps.keys():
            if map != None:
                map.sort()
            map = test_to_maps[line]
        elif line != '':
            map.insert(line.split(' '))

def part1():
    min_loc = sys.maxsize
    for seed in seeds:
        soil = seed_to_soil.get(seed)
        fertilizer = soil_to_fertilizer.get(soil)
        water = fertilizer_to_water.get(fertilizer)
        light = water_to_light.get(water)
        temperature = light_to_temperature.get(light)
        humidity = temperature_to_humidity.get(temperature)
        location = humidity_to_location.get(humidity)
        min_loc = min(min_loc, location)
    return min_loc

def read_portions(input):
    read_maps = []
    read_map = []
    for line in input:
        if line !='':
            if not line[0].isdigit():
                read_map.sort(key=itemgetter(1))
                read_maps.append(read_map)
                read_map = []
            else:
                mapped, start, length = map(int, line.split(' '))
                mapped -= start
                read_map.append((mapped, portion.closedopen(start, start+length)))
    read_map.sort(key=itemgetter(1))
    read_maps.append(read_map)
    return read_maps


def get_mapped_ranges(rngs, map):
    ranges = deque(rngs)
    i = 0
    found_range = []
    while i < len(ranges):
        old_len = len(ranges)
        range = ranges[i]
        for mapped_range in map:
            if range.overlaps(mapped_range[1]):
                del ranges[i]
                overlap = range & mapped_range[1]
                difference = range - mapped_range[1]
                overlap = overlap.replace(lower = overlap.lower+mapped_range[0], upper = overlap.upper+mapped_range[0])
                found_range.append(overlap)
                for prt in difference:
                   ranges.insert(i, prt)
        if len(ranges) == old_len:
            i+=1
    return list(ranges) + found_range

def part2():
    soil = get_mapped_ranges(seeds, seed_to_soil)
    fertilizer = get_mapped_ranges(soil, soil_to_fertilizer)
    water = get_mapped_ranges(fertilizer, fertilizer_to_water)
    light = get_mapped_ranges(water, water_to_light)
    temperature = get_mapped_ranges(light, light_to_temperature)
    humidity = get_mapped_ranges(temperature, temperature_to_humidity)
    location = get_mapped_ranges(humidity, humidity_to_location)
    return min(location, key=itemgetter(0)).lower

if __name__ == "__main__":
    puzzle_input = open("input/05.txt").read().splitlines()
    seeds = list(map(int, puzzle_input[0].replace('seeds: ', '').split()))
    read(puzzle_input[2:])
    print(part1())

    seeds = list(zip(seeds[::2], seeds[1::2]))
    # part 2

    for i, seed in enumerate(seeds):
        seeds[i] = portion.closedopen(seed[0], seed[0]+seed[1])
    seeds.sort()
    maps = read_portions(puzzle_input[3:])
    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = read_portions(puzzle_input[3:])

    print(part2())
    