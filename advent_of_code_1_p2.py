#!/usr/bin/env python

def adds_up_to_2020(expense_report):
    for x in expense_report:
        for y in expense_report:
            for z in expense_report:
                if x + y + z == 2020:
                    return x * y * z

f = open('d1_input.txt', 'r') # will open d1_input.txt
if f.mode == 'r': # checks the mode for the file
    contents = f.read() # reads the content of the file
    contents_list = contents.split()
    expense_report = [int(i) for i in contents_list] # list comprehension to convert string to integer

print(adds_up_to_2020(expense_report))