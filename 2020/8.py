instructions = open('input-8.txt').readlines()



def get_instruction(line):
    acc = 0
    pc = 1
    if line.startswith('jmp '):
        pc = int(line.replace('jmp ',''))
    elif line.startswith('acc '):
        acc = int(line.replace('acc ',''))
    return (pc, acc)

def fix_instruction(instruction):
    if instruction.startswith('jmp '):
        return instruction.replace('jmp ','nop ')
    return instruction.replace('nop ','jmp ')
    

def run_program(instructions):
    accumulator = 0
    program_counter = -1
    instructions_seen = set()
    instruction = (1, 0)

    while program_counter not in instructions_seen and program_counter < len(instructions):
        # store instruction as seen
        instructions_seen.add(program_counter)

        # apply instruction
        program_counter += instruction[0]
        accumulator += instruction[1]

        # get next instruction
        if program_counter < len(instructions):
            instruction = get_instruction(instructions[program_counter])
    return (program_counter, accumulator, program_counter in instructions_seen)
    
print('(program_counter, accumulator, has_cycle):')
print(run_program(instructions))

pc, ac, has_cycle = None, None, None
for ic in range(len(instructions)):
    fixed_instructions = instructions[:ic] + [fix_instruction(instructions[ic])] + instructions[ic +1 :]
    pc, ac, has_cycle = run_program(fixed_instructions)
    if not has_cycle:
        break

print('(program_counter, accumulator, has_cycle):')    
print(pc, ac, has_cycle)