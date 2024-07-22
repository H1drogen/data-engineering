

def deep_total(array):
    count = 0
    for num in array:
        if isinstance(num, list):
            count += deep_total(num)
        else:
            count += num
    return count
