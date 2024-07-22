

def deep_includes(stuff, target):
    for item in stuff:
        if item == target:
            return True
        if isinstance(item, list):
            return deep_includes(item, target)
    return False