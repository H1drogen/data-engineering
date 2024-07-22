import string


def sentence_to_camel_case(sentence, boolean):
    sentence = sentence.split()
    if boolean:
        for word in sentence:
            sentence[sentence.index(word)] = word.capitalize()
        return ''.join(sentence)
    else:
        return sentence[0].lower() + sentence_to_camel_case(' '.join(sentence[1:]), True)
