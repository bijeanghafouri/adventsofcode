import os
import sys

# with open(sys.argv[1], 'r') as f:
#    data = f.read()

# read input
fileObject = open("day1/input.txt", "r")
data = fileObject.read()

# transform to int


def Convert(string):
    li = list(string.split("\n"))
    return li


data = Convert(data)

# last item is null
data.remove('')
for i in range(0, len(data)):
    data[i] = int(data[i])


# Functions
def rounding(number, direction='down'):
    if isinstance(number, int) == True:
        return(int(number))
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
        return(int(round_number))


def get_fuel(mass):
    first_step = (mass / 3)
    second_step = rounding(first_step, direction='down')
    final = second_step - 2
    return(final)


def get_sum_fuel(data_list):
    fuel_list = []
    total = 0
    for i in data:
        fueled = get_fuel(i)
        fuel_list.append(fueled)
    for ele in range(0, len(fuel_list)):
        total = total + fuel_list[ele]
    return(total)


final_result = get_sum_fuel(data)
print(final_result)
