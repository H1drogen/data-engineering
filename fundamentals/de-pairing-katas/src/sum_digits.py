def sum_digits(number):
    count = 0
    for digit in str(number):
        if digit.isnumeric():
            count += int(digit)
    return count

