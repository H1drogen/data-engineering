
def sum_int(num):
    if num == 0:
        return 0
    return num + sum_int(num-1)
