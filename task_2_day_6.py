import string

f = open("Day 6\\puzzle.txt", "r")
forms = f.readlines()
form = ""

sorted_forms = []
form_full = ""
final_sum = []
forms_delimited = []

for form in forms:
    if form != "\n":
        form_full += form

    else:
        sorted_forms.append(form_full)
        form_full = ""

for form in sorted_forms:
    formatted_form = form.split('\n')[0:-1]
    string = formatted_form[0]
    for x in range (1,len(formatted_form)):
        new_string = ''.join(set(string).intersection(formatted_form[x]))
        string = new_string
    print(formatted_form)
    final_sum.append(len(string))

print(sum(final_sum))