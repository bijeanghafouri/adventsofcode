import math
import os
import sys

print('Begin Script')
# with open(sys.argv[1], 'r') as f:
#    contents = f.read()


def rounding(number, direction='down'):
    if isinstance(number, int) == True:
        print(number)
    else:
        if direction == 'down':
            mod = number % 1
            round_number = number - mod

        elif direction == 'up':
            mod = number % 1
            round_number = number - mod + 1

        elif direction == 'auto':
            if (number % 1) >= 0.5:
                mod = number % 1
                round_number = number - mod + 1
            else:
                mod = number % 1
                round_number = number - mod
        return(round_number)


num = 3.4
print(rounding(num, direction='up'))


def get_fuel(mass):
    first_step = (mass / 3)
    second_step = rounding(first_step, direction='down')
    final = second_step - 2
    return(final)


print(get_fuel(33))


print('All done!')
