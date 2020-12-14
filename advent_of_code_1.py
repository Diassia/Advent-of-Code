#!/usr/bin/env python
 
def alternate(expense_report):
    for x in expense_report:
        for y in expense_report:
            if x + y == 2020:
                return x * y

f = open('d1_input.txt', 'r') # will open d1_input.txt
if f.mode == 'r': # checks the mode for the file
    contents = f.read() # reads the content of the file
    contents_list = contents.split()
    expense_report = [int(i) for i in contents_list] # list comprehension to convert string to integer

print(alternate(expense_report))

# def number_to_test(number, expense_report):
#     selected_number = number
#     for number in expense_report:
#         if number + selected_number == 2020:
#             return number * selected_number

# def adds_up_to_2020(expense_report):
#     for number in expense_report:
#         result_number = number_to_test(number, expense_report)
#         if result_number != None:
#             return result_number

# def alternate_2(expense_report):
#     [x * y for x in expense_report for y in expense_report if x + y == 2020]