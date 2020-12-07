import re
import string

f = open("Day 6\\puzzle.txt", "r")
forms = f.readlines()

sorted_forms = []
form_full = ""
final_sum = []

#print(forms)

for form in forms:
    if form != "\n":
        form_full += form

    else:
        sorted_forms.append(form_full)
        form_full = ""

for form in sorted_forms:
    print("New Form!")
    total_yes = 0
    for x in list(string.ascii_lowercase):
        if x in form:
            total_yes += 1
    final_sum.append(total_yes)
    print(total_yes)

print(sum(final_sum))