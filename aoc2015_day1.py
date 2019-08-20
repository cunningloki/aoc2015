import re

input_string = 'advent_01.txt'

with open(input_string, 'r') as input_file:
    for line in input_file:

        open_parenthesis = re.findall(r'\(', line)
        close_parenthesis = re.findall(r'\)',line)

        open_parenthesis_count = len(open_parenthesis)
        close_parenthesis_count = len(close_parenthesis)

        floor = open_parenthesis_count - close_parenthesis_count
        print("Santa, go to floor " + str(floor))

input_file.close()

input_string = 'advent_01.txt'

with open(input_string, 'r') as input_file:
    for line in input_file:
        print("Floor #: " + str(len(line.split('('))-len((line.split(')')))))

import operator

input_string = 'advent_01.txt'

floor = 0
char_count = 0
in_basement = False

with open(input_string, 'r') as input_file:
    for line in input_file:
        for char in line:
            if operator.eq('(',char):
                floor += 1
            elif operator.eq(')',char):
                floor -= 1
            else:
                print('invalid input')
            char_count += 1
            if(floor < 0):
                if not in_basement:
                    in_basement = True
                    print("Entered basement at char: " + str(char_count))

    print("Floor: " + str(floor))
input_file.close()

