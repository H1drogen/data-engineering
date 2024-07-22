
def contains_char(word, letter):
    if word[0].lower() == letter.lower():
       return True
    if word == word[len(word) - 1]:
        return False
    return contains_char(word[1:], letter)