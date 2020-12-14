import re

def text_file():
    f = open('d2_input.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        contents_list = contents.splitlines()
    return contents_list

def count_no_correct_passwords():
    count = 0
    contents_list = text_file()

    for i in contents_list:
        string = i
        
        contentsRegex = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w*)')
        m = re.match(contentsRegex, string)

        min_match = m.group('min')
        max_match = m.group('max')
        letter_match = m.group('letter')
        password_match = m.group('password')

        if (password_match[int(min_match) - 1] == letter_match) and (password_match[int(max_match) - 1] == letter_match):
            continue
        elif (password_match[int(min_match) - 1] == letter_match) or (password_match[int(max_match) - 1] == letter_match):
            count += 1
        else:
            continue

    return count

print(count_no_correct_passwords())