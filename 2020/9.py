numbers = list(map(int, open('input-9.txt').readlines()))
#print(numbers)

preamble = 25
i = preamble
prev_numbers = set(numbers[:i])
check = True
current_num = None

while i < len(numbers) -1 and check:
    current_num = numbers[i]
    # check
    check = False
    for num in prev_numbers:
        check = check or ((numbers[i] - num) in prev_numbers)

    # move frame
    prev_numbers.remove(numbers[i - preamble])
    prev_numbers.add(current_num)
    i +=1

frist_wrong_num = current_num
print('First number to violate rule:')
print(frist_wrong_num)

i=0;
contiguous_start, contiguous_end= 0, 1
found = False
while contiguous_start < len(numbers) -1 and not found:
    contiguous_end, contiguous_sum = contiguous_start + 1, 0
    while contiguous_sum < frist_wrong_num and contiguous_end <= len(numbers):
        # calculate contiguous_sum
        contiguous_sum = sum(numbers[contiguous_start: contiguous_end + 1])
        contiguous_end += 1
    found = contiguous_sum == frist_wrong_num
    contiguous_start += 1

print(found, numbers[contiguous_start-1], numbers[contiguous_end-1])
sorted_contiguous = sorted(numbers[contiguous_start -1: contiguous_end])
encryltion_num = sorted_contiguous[0] + sorted_contiguous[-1]
print(encryltion_num)