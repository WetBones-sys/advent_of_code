f = open("Day 5\\puzzle.txt", "r")
passes = f.readlines()

seat_IDs = []

def check_seat(seat_code):
    row_numbers = [*range(0,128,1)]
    for x in range(0,7):
        if seat_code[x] == 'F':
            row_numbers = row_numbers[0:int(len(row_numbers)/2)]
        elif seat_code[x] == 'B':
            row_numbers = row_numbers[int(len(row_numbers)/2):len(row_numbers)]
        else:
            print("Error!!!")
            return None
        

    column_numbers = [*range(0,8,1)]
    
    for y in range(7,10):
        if seat_code[y] == 'L':
            column_numbers = column_numbers[0:int(len(column_numbers)/2)]
        elif seat_code[y] == 'R':
            column_numbers = column_numbers[int(len(column_numbers)/2):len(column_numbers)]
        else:
            print("Error!!! (But in the Column Section this time)")
            return None
    seat_number = (row_numbers[0] * 8) + column_numbers[0]
    return seat_number

for boarding_pass in passes:
    seat_IDs.append(check_seat(boarding_pass))

seat_IDs.sort()

for z in range (min(seat_IDs),max(seat_IDs)):
    if z not in seat_IDs:
        print(z)
