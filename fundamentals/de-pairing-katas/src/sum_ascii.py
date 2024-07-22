def sum_ascii(List):
    highest_count = [0, 'word']
    for word in List:
        count = 0
        for char in word:
            count += ord(char.lower())
        if count > highest_count[0]:
            highest_count = [count, word]

    return highest_count[1]
