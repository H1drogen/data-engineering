def indexer(text):
    if text == '':
        return
    i = 0
    while text[i].isspace():
        i += 1
    yield i
    while i < len(text) - 1:
        if text[i].isspace():
            while text[i].isspace():
                i += 1
                if i > len(text) - 1:
                    return
            yield i
        else:
            i += 1


def cool_cat(*args):
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                yield (key, value)
        elif isinstance(arg, str):
            if len(arg) == 1:
                yield arg
            else:
                for arg2 in arg:
                    yield from cool_cat(arg2)
        elif isinstance(arg, list):
            for arg2 in arg:
                yield from cool_cat(arg2)
