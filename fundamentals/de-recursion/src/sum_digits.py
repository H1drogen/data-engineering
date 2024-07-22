
def sum_digits(nums):
    if nums <= 0:
        return 0
    return nums % 10 + sum_digits(int(nums / 10))