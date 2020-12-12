def second_number_increment(no2_index, expense_report):
    index = no2_index
    return expense_report[no2_index]


def number_to_test(number, expense_report):
    no2_index = 0

    number_1 = number # original number to test

    count = 0

    for index in range(len(expense_report[0:-1])):
        while count < len(expense_report):
            number_2 = second_number_increment(no2_index, expense_report) # changes number 2 by one index
            number_3 = expense_report[index + 2]

            if number + number_2 + number_3 == 2020:
                return number * number_2 * number_3
            else:
                count += 1
                no2_index += 1

def adds_up_to_2020(expense_report):
    for number in expense_report:
        result_number = number_to_test(number, expense_report)
        if result_number != None:
            return result_number