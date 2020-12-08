f = open("Day 8\\puzzle.txt", "r")
instructions = f.readlines()
original_instructions = instructions[:]

instruction_set = []

# Run lines

def run_code(instructions):

    x = 0 # current instruction index
    xs = [] # previous instruction indeces
    accumulator = 0

    while x < len(instructions):

        #print(x)
        instruction = instructions[x] # current instruction

        if x in xs: # if looped, stop
            #print(x)
            return None
        else: # run code
            xs.append(x)
            if instruction[0:3] == 'acc': # if acculumator instruction
                accumulator += int(instruction[4:])
                x += 1
            elif instruction[0:3] == 'jmp': # if jump instruction
                x += int(instruction[4:])
            else: # if nop instruction
                x += 1
    return accumulator

for x in range(0, len(instructions)):
    if instructions[x][0:3] == 'jmp': # flip previous line
        instructions[x] = 'nop ' + instructions[x][4:]
    elif instructions[x][0:3] == 'nop':
        instructions[x] = 'jmp ' + instructions[x][4:]
    instruction_set.append(instructions)
    instructions = original_instructions[:]

print(instruction_set[0])
print(instruction_set[1])
print(instruction_set[2])

for modified in instruction_set:
    if run_code(modified) != None:
        print(run_code(modified))