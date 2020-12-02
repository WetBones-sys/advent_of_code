f = open("Day 2\puzzle.txt", "r")
passwords = f.readlines()
answerCount = 0

for x in passwords: # for each line
    line = x.split(' ') # split by space
    necessaryLetter = line[1][0] # letter needed
    countHere = 0
    numbers = line[0].split('-') # remove -'s from rule
    minimumCount = numbers[0]
    maximumCount = numbers[1]

    for letter in line[2]:
        if letter == necessaryLetter:
            countHere += 1
    
    print(str(countHere) + " " + minimumCount + " " + maximumCount)

    if countHere >= int(minimumCount) and countHere <= int(maximumCount):
        answerCount += 1
        print(answerCount)

