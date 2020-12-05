import re

f = open("Day 4\\puzzle.txt", "r")
passports = f.readlines()

sorted_passports = []
num_of_valid = 0
passport_full = ""

for passport in passports:
    if passport != "\n": # Create passport
        passport_full += passport

    else:
        sorted_passports.append(passport_full)
        passport_full = ""

#print(len(sorted_passports))

for sorted_passport in sorted_passports:

    if re.search("byr:",sorted_passport) != None: # Birth Year
        birthyears = re.findall(r"byr:\d{4}[\s\n]",sorted_passport)
        if int(birthyears[0][4:]) >= 1920 and int(birthyears[0][4:]) <= 2002: # valid birth years
            if re.search("iyr:",sorted_passport) != None: # Issue Year
                issueyears = re.findall(r"iyr:\d{4}[\s\n]",sorted_passport)
                if int(issueyears[0][4:]) >= 2010 and int(issueyears[0][4:]) <= 2020: # valid issue year
                    if re.search("eyr:",sorted_passport) != None: # Expiration Year
                        expirationyears = re.findall(r"eyr:\d{4}[\s\n]",sorted_passport)
                        if int(expirationyears[0][4:]) >= 2020 and int(expirationyears[0][4:]) <= 2030: # valid expiration year
                            if re.search("hgt:",sorted_passport) != None: # Height
                                height = re.findall(r"hgt:[\d]+in|hgt:[\d]+cm",sorted_passport)
                                if height != []: # Ends in in or cm
                                    torf = False
                                    if re.findall(r"hgt:[\d]+in",height[0]) != []: # if in inches
                                        value =  int(re.findall(r"hgt:[\d]+in",height[0])[0][4:-2])
                                        if value >= 59 and value <= 76:
                                            #print(value)
                                            torf = True
                                    elif re.findall(r"hgt:[\d]+cm",height[0]) != []: # if in centimetres
                                        value =  int(re.findall(r"hgt:[\d]+cm",height[0])[0][4:-2])
                                        if value >= 150 and value <= 193:
                                            torf = True
                                    if torf == True: # then height is valid
                                        if re.search("hcl:",sorted_passport) != None: # Hair Colour
                                            haircolour = re.findall(r"hcl:#([0-9a-f]{6})",sorted_passport)
                                            if haircolour != []: # if correct hair colour
                                                if re.search("ecl:",sorted_passport) != None: # Eye Colour
                                                    valid_eyes = ["amb","blu","brn","gry","grn","hzl","oth"]
                                                    eye_colour = re.findall(r"ecl:...",sorted_passport)[0]
                                                    if (eye_colour[4:7] in valid_eyes) and len(eye_colour) == 7: # if valid eye colour
                                                        if re.search("pid:",sorted_passport) != None: # Passport ID
                                                            passport_ID = re.findall(r"pid:(\d){9}\s",sorted_passport)
                                                            if passport_ID != []: # Valid ID
                                                                num_of_valid += 1
                                                                print(num_of_valid)

