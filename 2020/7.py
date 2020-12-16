import re
import itertools

# Bag class for reccording what bags are contained
class Bag:
    bags = {} # class level dictionary of all available bags (there is just 1 in total not 1 per bag)

    def __init__(self, colour):
        self.colour = colour
        self.contains = {}

    def process_rule(bag_rule): #class level method for processing a bag rule
        bag_rule = bag_rule.replace('no other bags', '').replace('contain', 'contain,') # making rule easier to process by removing the lingustrc difference of the first bag (or no bags)
        m = re.search(r'(.+?) bags contain', bag_rule) # find what bags the rule talks about
        bag = Bag.add_bag(m.group(1))
        contains = re.findall(r', ([0-9]+?) (.+?) bag', bag_rule) # find the bags contained
        for contained_bag in contains:
            Bag.add_bag(contained_bag[1])
            bag.contains[contained_bag[1]] = int(contained_bag[0])

    def add_bag(colour): # class level method for adding a new bag
        if not colour in Bag.bags:
            Bag.bags[colour] = Bag(colour)
        return Bag.bags[colour]

    # functions to allow printing bag objects used when checking it was doing the right thing
    def __repr__(self):
        return str(self.colour) + ' ' +str(self.contains)
    def __str__(self):
        return str(self.colour) + '\n' +str(self.contains) + '\n'

# read & process all bag rules
bag_rules = open('input-7.txt').readlines()
for bag_rule in bag_rules:
    Bag.process_rule(bag_rule)
    
to_find = 'shiny gold'
number_of_combos = 0;
found = False

for colour, bag in Bag.bags.items():
    found = False
    contains = list(bag.contains)
    while not found and len(contains) > 0:
        containing_bag = contains.pop(0)
        found = containing_bag == to_find
        contains.extend(list(Bag.bags[containing_bag].contains))
    number_of_combos += found

print('Bag colors that can eventually contain at least one shiny gold bag:')
print(number_of_combos)
print()


bag_count = 0
bag = Bag.bags[to_find]
contains = list(bag.contains.items())
while len(contains) > 0:
    containing_bag = contains.pop(0)
    bag_count += containing_bag[1]
    for _ in range(containing_bag[1]):
        contains.extend(Bag.bags[containing_bag[0]].contains.items())
        
print('Number of individual bags required inside a single shiny gold bag:')
print(bag_count)