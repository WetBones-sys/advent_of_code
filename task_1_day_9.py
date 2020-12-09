f = open("Day 9\\puzzle.txt", "r")
numbers = f.readlines()
stripped = []

for number in numbers:
    stripped.append(number[:-1])

x = 25

while x < len(stripped):

    # Initialise values

    prior = stripped[x-25:x] # prior values 
    #print(prior)
    value = int(stripped[x]) # current value
    match = False # whether or not it is valid

    # Check validity

    for num in prior: # For each number in the prior
        for num2 in prior: # Check on each other to see if it adds to value
            if num != num2: # Make sure it doesn't check on itself
                add = int(num) + int(num2)
                if add == value: # if they add to the required value
                    #print(num + " + " + num2)
                    match = True
    if match == True:
        x += 1

    if match == False:
        print(value)
        x = len(stripped) 