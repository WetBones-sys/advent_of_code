f = open("Day 3\\puzzle.txt", "r")
map = f.readlines()
position = [0,0]
num_of_trees = 0

#print(map)

#print(len(map))
#print(len(map[0]))
#print(len(map[322]))

for line in map: # each line from top to bottom
    position[0] = position[0] + 2
    position[1] = position[1] + 1 # new position

    if position[1] >= len(map[322]):
        position[1] = position[1] - len(map[322])

    print("X = " + str(position[0]) + ". Y = " + str(position[1]))

    if not(position[0] >= len(map)):
        if map[position[0]][position[1]] == '#':
            num_of_trees += 1

    print(num_of_trees)