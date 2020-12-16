import re

instructions = open('input-14.txt').readlines()


def value_mask(value, mask):
    binary_value = list(format(int(value), '036b'))
    for i, (v,m) in enumerate(zip(binary_value,mask)):
        if m in ('0', '1'):
            binary_value[i] = m
    return int(''.join(binary_value),2)

mask = ''
registers = {}

for instruction in instructions:
    mask_match = re.search(r'mask = (.*)', instruction)
    mem_match = re.search(r'mem\[(.+)\] = (.+)', instruction)
    if mask_match:
        mask = mask_match.group(1)
    elif mem_match:
        registers[mem_match.group(1)] = value_mask(mem_match.group(2), mask)


print('sum of values: ', sum(registers.values()))


def address_mask(address, mask):
    def find_addresses(bin_addr):
        if len(bin_addr) == 1:
            if bin_addr[0] == 'X':
                return [['0'],['1']]
            else:
                return [list(bin_addr)]
        else:
            result_addr = []
            addresses = find_addresses(bin_addr[:-1])
            address_ends = find_addresses(bin_addr[-1])
            for address in addresses:
                for address_end in address_ends:
                    result_addr.append(address + address_end)
            return result_addr
    
    binary_address = list(format(address, '036b'))
    for i, (a,m) in enumerate(zip(binary_address,mask)):
        if m in ('1', 'X'):
            binary_address[i] = m
    
    return map(lambda ba: int(''.join(ba),2), find_addresses(binary_address))

mask = ''
registers = {}

for instruction in instructions:
    mask_match = re.search(r'mask = (.*)', instruction)
    mem_match = re.search(r'mem\[(.+)\] = (.+)', instruction)
    if mask_match:
        mask = mask_match.group(1)
    elif mem_match:
        for a in address_mask(int(mem_match.group(1)), mask):
            registers[a] = int(mem_match.group(2))


print('sum of values: ', sum(registers.values()))