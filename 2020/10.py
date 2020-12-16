from functools import reduce


adapters = sorted(map(int, open('input-10.txt').readlines()))

adapters.insert(0, 0)
adapters.append(max(adapters) + 3)


differences = {1 : 0, 2 : 0, 3: 0}

for i, adapter in enumerate(adapters[:-1]):
    diff = adapters[i+1] - adapters[i]
    differences[diff] += 1

print(differences)

print('Number of 1-jolt differences multiplied by the number of 3-jolt differences:')
print(differences[1] * differences[3])

# def try_adapters(adapter_list, start=True):
    # if len(adapter_list) <= 1:
        # return [adapter_list]
    
    # first = adapter_list[0]
    # end = adapter_list[-1]
    # rest = adapter_list[1:-1]
    # permutations = []
    # possible = []
    
    # for i, p in enumerate(rest):
        # if p - first > 3:
            # break
        # perms = try_adapters()
        # permutations.extend(rest[i] + print(l2[0:i] + l2[i+1:])
        # possible.append(p)
        # print(rest[0:i] + rest[i:])
    
    # print(first)
    # print(rest)
    # print(possible)

    # #return permutations
    
def try_adapters(adapter_list):
    if len(adapter_list) <= 2:
        return [adapter_list]
    
    first = adapter_list[0]
    last = adapter_list[-1]
    possible_2nd_last = []
    combos = []
    for p in reversed(adapter_list[:-1]):
        if last - p > 3:
            break
        possible_2nd_last.append(p)
        to_try = list(filter(lambda n: n < p, adapter_list))
        to_try.append(p)
        #print(to_try)
        combos.extend(try_adapters(to_try))
        #print(combos)
    for c in combos:
        c.append(last)
    return combos

#print('valid combinations of adapters')
#print(len(try_adapters(adapters)))

split_adapters = []
adap = []
prev = adapters[0]
for a in adapters:
    if a-prev < 3:
        adap.append(a)
    else:
        split_adapters.append(adap)
        adap=[a]
    prev = a
    
sub_list_combo_lengths = [len(try_adapters(sa)) for sa in split_adapters]
print(reduce((lambda x, y: x * y), sub_list_combo_lengths))
