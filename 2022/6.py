import string

def first_chars(sequence, first_no):
    first_chars = []
    for i, char in enumerate(sequence, start=1):
        first_chars.append(char)
        if len(first_chars) > first_no:
            first_chars.pop(0)
        if len(set(first_chars)) == first_no:
            return i

sequence = open('6.txt').read()
print(first_chars(sequence, 4))
print(first_chars(sequence, 14))