import re
import math

class Ranges:
    def __init__(self, ranges):
        self.number_ranges = []
        for range in ranges:
            split_rng = range.split('-')
            self.number_ranges.append((int(split_rng[0]), int(split_rng[1])))

    def valid(self, num):
        valid = False
        for r in self.number_ranges:
            valid = valid or r[0] <= num <= r[1]
        return valid

    def __repr__(self):
        return str(self.number_ranges)

rules = {}
your_ticket = []
your_ticket_rules = []
nearby_tickets = []

def invalid_fields(ticket):
    invalid_values = []
    for field in ticket:
        valid_field = False
        for _, range in rules.items():
            valid_field = range.valid(field)
            if valid_field:
                break
        valid_ticket = valid_field
        if not valid_field:
            invalid_values.append(field)
    return invalid_values

def valid_ticket(ticket):
    return len(invalid_fields(ticket)) == 0

ticket_data = open('input-16.txt').read().split('\n')
i = 0
while i< len(ticket_data):
    if ticket_data[i] == '':
        break
    match = re.search(r'(.+): ', ticket_data[i])
    match_ranges = re.findall(r'([0-9]+-[0-9]+)+', ticket_data[i])
    rules[match.group(1)] = Ranges(match_ranges)

    i+= 1
i+=2

your_ticket = list(map(int,ticket_data[i].split(',')))
i+=3

while i< len(ticket_data):
    nearby_tickets.append(list(map(int,ticket_data[i].split(','))))
    i+= 1

invalid = []
for t in nearby_tickets:
    invalid.extend(invalid_fields(t))
print(sum(invalid))

#part 2
field_names = []
valid_tickets = list(filter(lambda t: valid_ticket(t), nearby_tickets))
valid_tickets.append(your_ticket)

valid_fields = [set() for _ in range(len(valid_tickets[0]))]

for i in range(len(valid_tickets[0])):
    fields_to_test = [t[i] for t in valid_tickets]
    for rule_name, rule in rules.items():
        all_field_valid = True
        for f in fields_to_test:
            all_field_valid = all_field_valid and rule.valid(f)
            if not all_field_valid:
                break
        if all_field_valid:
            valid_fields[i].add(rule_name)

assert len(valid_fields) == len(valid_tickets[0])

changed = True
while changed:
    changed = False
    for i, field in enumerate(valid_fields):
        if len(field) == 1:
            for j, other_field in enumerate(valid_fields):
                if i != j and tuple(field)[0] in other_field:
                    valid_fields[j] = other_field - field
                    changed=True

assert sum([len(f) for f in valid_fields]) == len(valid_fields)

ticket_field_multiply = [your_ticket[i] if tuple(f)[0].startswith('departure') else 1 for i, f in enumerate(valid_fields)]
print(math.prod(ticket_field_multiply))