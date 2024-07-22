def alternate_case(word: str):
    new_word = ''
    for index in range(len(word)):
        if index % 2 == 0:
            new_word += word[index].upper()
        else:
            new_word += word[index].lower()

    return new_word
