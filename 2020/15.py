def nth_number_spoken(starting_num, nth):
    def get_next_counters(num):
        prev_counter = number_positions.get(num, num_counter)
        return prev_counter, num_counter, num, num_counter+1

    num_counter, prev_num_counter = 0, 0
    number_positions = {}
    prev_num = None

    for num in starting_num:
        prev_num_counter, number_positions[num], prev_num, num_counter = get_next_counters(num)

    while num_counter < nth:
        num = num_counter - prev_num_counter -1
        prev_num_counter, number_positions[num], prev_num, num_counter = get_next_counters(num)

    return num

print(nth_number_spoken([1,0,15,2,10,13], 30000000))