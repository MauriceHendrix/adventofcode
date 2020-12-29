import re
from pyparsing import Suppress, Forward, Group, oneOf, pyparsing_common, infixNotation, opAssoc, Literal, ParseException, Optional, OneOrMore 

# rule_list, messages = open('input-19.txt').read().split('\n\n')
# rule_list, messages = rule_list.split('\n'), messages.split('\n')

# rules = {}


# def process_rule(rule_text):
    # parts = rule_text.split(' ')
    # my_rule = rules[int(parts[0])] = rules.get(int(parts[0]), Forward())
    # for r in parts[1:]:
        # rule_part = rules[int(r)] = rules.get(int(r), Forward())
        # my_rule += rule_part
    # return my_rule
    


# rule_list.insert(0, '999: "P"')
# # process rules
# for i, rule_str in enumerate(rule_list):
    # if rule_str.startswith('0:'):
        # rule_str += " 999"
    # if rule_str != '':
        # colon = rule_str.find(':')
        # index = int(rule_str[0: colon])
        # rule_text = rule_str[colon +2:].strip()
        
        # rules[index] = rules.get(index, Forward())
        # if rule_text.startswith('"'):
            # rules[index] <<= Literal(rule_text.replace('"', ''))
        # else:
            # rule_parts = rule_text.split('|')
            # my_rule = process_rule(rule_parts[0].strip())
            # for rule_part in rule_parts[1:]:
                # my_rule = my_rule | process_rule(rule_part.strip())
            # rules[index] <<= my_rule

# rules[8] <<= rules[42] | rules[42] + rules[8]
# rules[11] <<= rules[42] + rules[31] | rules[42] + rules[11] + rules[31]



# # messages
# count_matches = 0
# matches_found = []
# rules[0].setParseAction(lambda toks: "".join(toks))
# for message in messages:
    # if message != '':
        # message += 'P'
        # #print(message)
        # try:
            # m = rules[0].searchString(message)
            # count_matches+= len(m) == 1
            # matches_found.append((message,m))
        # except ParseException:
            # pass

# print("# messages matching rule: ",count_matches)

rules={}

def process_rule_re(rule_text):
    parts = list(map(int, rule_text.split(' ')))
    my_rule = r''
    for part in parts:
        if int(part) in rules:
            my_rule += rules[int(part)]
        else:
            return r''
    return my_rule

# rule_list = open('input-19.txt').readlines()
# rule_list, messages = rule_list[:rule_list.index('\n')], rule_list[rule_list.index('\n')+1:]
rule_list, messages = open('input-19.txt').read().split('\n\n')
rule_list, messages = rule_list.split('\n'), messages.split('\n')

changed = True
while changed:
    old_rules = rules.copy()
    changed=False
    for i, rule_str in enumerate(rule_list):
        if rule_str != '':
            colon = rule_str.find(':')
            index = int(rule_str[0: colon])
            rule_text = rule_str[colon +2:].strip()
            if index not in rules:
                if rule_text.startswith('"'):
                    rules[index] =r'{}'.format(rule_text.replace('"', ''))
                    changed = True
                else:
                    rule_parts = rule_text.split('|')
                    my_rule = process_rule_re(rule_parts[0].strip())
                    for rule_part in rule_parts[1:]:
                        assert not '|' in rule_part
                        other_rule_part = process_rule_re(rule_part.strip())
                        if my_rule and other_rule_part:
                            my_rule = my_rule + r'|' + other_rule_part
                        else:
                            my_rule = r''
                    if my_rule:
                        changed = True
                        rules[index] = r'(' + my_rule + r')'

rules[8] = rules[8] + r'?+'
assert rules[11] == r'(' + rules[42] + rules[31] + r')'
rules[11] = r'(' + rules[42] + rules[31] + r'?+'


for i, r in rules.items():
    rules[i] = '('+ r + r')\Z'

#rules[8] = print(rules[8].replace(r'\Z', r'+\z'))
print(rules[11])

count_matches_regex = []
for m in messages:
    if m != '\n':
        #print('->'+str(m))
        match = re.match(rules[0], m)
        if match:
            count_matches_regex.append(match.group(0))
print(len(count_matches_regex))