f = open("Day 7\\puzzle.txt", "r")
bags = f.readlines()

bags_split = []
num_of_gold = 0
for bag in bags:
    bags_split.append(bag.split(' contain ')) # splits into bag types

# Each line is in format: 'adjective colour bags','number adjective colour bags'(any number)

num_of_bags = 0

def count_bags(bag_name):
    global num_of_bags
    for bag in bags_split:
        if bag_name in bag[0]:
            for sub_bag in bag[1:][0].split(', '): # for each smaller bag
                if sub_bag[0] != 'n':
                    num_of_this_bag = int(sub_bag[0])
                    num_of_bags += num_of_this_bag # add number of that bag

                    # Check smaller bag numbers
                    bag_split = sub_bag.split(' ')
                    new_bag_name = bag_split[1] + " " + bag_split[2]
                    
                    for x in range (0,int(sub_bag[0])):
                        count_bags(new_bag_name)

            return num_of_bags

print(count_bags('shiny gold'))