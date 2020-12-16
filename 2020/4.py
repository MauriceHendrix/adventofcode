import re

def passport_valid(passport):
    return 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport

def passport_validated(passport):
    try:
        valid = int(passport['byr']) >= 1920 and  int(passport['byr']) <= 2002 \
            and int(passport['iyr']) >= 2010 and  int(passport['iyr']) <= 2020 \
            and int(passport['eyr']) >= 2020 and  int(passport['eyr']) <= 2030 \
            and (passport['hgt'].endswith('cm') or passport['hgt'].endswith('in')) and passport['hgt'].replace('cm', '').replace('in', '').isnumeric() \
            and (passport['hgt'].endswith('in') or (int(passport['hgt'].replace('cm', ''))>= 150 and  int(passport['hgt'].replace('cm', '')) <= 193)) \
            and (passport['hgt'].endswith('cm') or (int(passport['hgt'].replace('in', ''))>= 59 and  int(passport['hgt'].replace('in', '')) <= 76)) \
            and len(passport['hcl']) == 7 \
            and passport['hcl'].startswith('#') \
            and passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') \
            and len(passport['pid']) == 9 and passport['pid'].isnumeric()
        int(passport['hcl'][1:], 16) # hcl is a hex number
    except (KeyError, ValueError):
        return False
    return valid
    
passports_found = []

f = open("input-4.txt", "r")
lines = f.readlines()
lines.append('\n')

passport = {}

for line in lines: 
    if line == '\n': 
        passports_found.append(passport) 
        passport = {}
    else:
        for field in line.split(' '):
            match = re.search(r'(.*):(.*)',field)
            assert match.group(1) not in passport
            passport[match.group(1)] = match.group(2)

print(len(passports_found))
valid_passports = [p for p in passports_found if passport_valid(p)]
print(len(valid_passports))
valid_passports = [p for p in passports_found if passport_validated(p)]
print(len(valid_passports))