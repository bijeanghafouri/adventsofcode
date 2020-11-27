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



hello = rounding(2.9, direction='down')
print(hello)