
def sum_consecutive_duplicates(numbers):
    i = 0
    numbers = numbers.copy()
    while i < len(numbers) - 1:
        count = 1
        while numbers[i] == numbers[i + 1]:
            numbers.pop(i + 1)
            count += 1
            if i == len(numbers) - 1:
                break
        numbers[i] = numbers[i] * count
        i += 1
    return numbers

def reduce_consecutive_duplicates(numbers):
    current_list = numbers
    while True:
        new_list = sum_consecutive_duplicates(current_list)
        if new_list == current_list:
            return new_list
        current_list = new_list