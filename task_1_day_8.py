f = open("Day 8\\puzzle.txt", "r")
instructions = f.readlines()

accumulator = 0
x = 0
xs = []

while x < len(instructions): # for each instruction
    instruction = instructions[x]

    # Check if already run

    if x in xs:
        print(accumulator)
        x = len(instructions)
    else:
        xs.append(x)

    # Run instruction

    if instruction[0:3] == 'acc': # if acculumator instruction
        accumulator += int(instruction[4:-1])
        x += 1
    elif instruction[0:3] == 'jmp': # if jump instruction
        x += int(instruction[4:-1])
    else: # if nop instruction
        x += 1