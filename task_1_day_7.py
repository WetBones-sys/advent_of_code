f = open("Day 7\\puzzle.txt", "r")
bags = f.readlines()

bags_split = []
num_of_gold = 0
for bag in bags:
    bags_split.append(bag.split(' contain ')) # splits into bag types

# Each line is in format: 'adjective colour bags','number adjective colour bags'(any number)

def check_bag(bag):
    gold = False
    for bag_type in bag[1:]:
        if 'shiny gold' in bag_type: # if it's in the direct rule
            gold = True # confirmed to work
        else: # if in a smaller bag
            super_split = bag_type.split(', ')
            for thing in super_split:
                supreme_split = thing.split(' ')
                for bag in bags_split:
                    if (supreme_split[1] in bag[0]) and (supreme_split[2] in bag[0]):
                        if check_bag(bag) == True:
                            gold = True
    return gold

for bag in bags_split:
    if check_bag(bag) == True:
        num_of_gold += 1

print(num_of_gold)