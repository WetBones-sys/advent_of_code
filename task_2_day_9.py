f = open("Day 9\\puzzle.txt", "r")
numbers = f.readlines()
stripped = []

for number in numbers:
    stripped.append(int(number[:-1]))

required_value = 14360655
x = 0

def getAllWindows(L):
    for w in range(1, len(L)+1):
        for i in range(len(L)-w+1):
            yield L[i:i+w]

subs = getAllWindows(stripped)

for subarray in subs:
    if len(subarray) != 1 and sum(subarray) == required_value:
        output = min(subarray) + max(subarray)
        print(output)