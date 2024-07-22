from typing import List

def nc_max(numbers: List):
    if len(numbers) == 0:
        return 0
    return max(numbers)


def nc_min(numbers: List):
    if len(numbers) == 0:
        return 0
    return min(numbers)
