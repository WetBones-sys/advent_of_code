f = open("Day 2\puzzle.txt", "r")
passwords = f.readlines()
answerCount = 0

for x in passwords: # for each line
    line = x.split(' ') # split by space
    numbers = line[0].split('-') # remove -'s from rule
    necessaryLetter = line[1][0]
    firstIndex = int(numbers[0])
    secondIndex = int(numbers[1])
    password = line[2]

    if password[firstIndex-1] == necessaryLetter or password[secondIndex-1] == necessaryLetter:
        if not(password[firstIndex-1] == necessaryLetter and password[secondIndex-1] == necessaryLetter):
            #print("Password = " + password + " Indeces = " + str(firstIndex) + " " + str(secondIndex) + " Letter = " + necessaryLetter )
            answerCount+=1

print(answerCount)