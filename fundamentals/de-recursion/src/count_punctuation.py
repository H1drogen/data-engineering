
def count_punctuation(word):
    punctuation = [",", ".", "!", "?"]
    if len(word) == 0:
        return 0
    if word[0] in punctuation:
        return 1 + count_punctuation(word[1:])
    return count_punctuation(word[1:])
