import os
import sys
# with open(sys.argv[1], 'r') as f:
#    data = f.read()

# read input
fileObject = open("input.txt", "r")
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
    # Set parameter and counter
    fuel_list = []
    total = 0
    # apply fuel fun to every element of list and save to list
    for i in data:
        fueled = get_fuel(i)
        fuel_list.append(fueled)
    # Get the sum
    for ele in range(0, len(fuel_list)):
        total = total + fuel_list[ele]
    # Return Result
    return(total)


# ------------ Part 2 -------------
new_fuel_list = []


def get_more_fuel(mass):
    first_step = (mass / 3)
    second_step = rounding(first_step, direction='down')
    final = second_step - 2
    # print(final)
    new_fuel_list.append(final)
    # print(new_fuel_list)
    if final > 6:
        init = final
        get_more_fuel(init)
        return(new_fuel_list)

# Get the sum


def get_total(list):
    total = 0
    for ele in range(0, len(list)):
        total = total + list[ele]
    return(total)


result = []
final_result = 0


def tmp(data):
    for i in data:
        fuel = get_more_fuel(i)
        one_total = get_total(fuel)
        result.append(one_total)
        return(result)


print(tmp(data))

if len(result) == len(data):
    final_result == get_total(result)
