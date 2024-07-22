def flip(func):
    def wrapper(*args):
        a=args[0]
        b=args[1]
        result=func(b, a)
        return result
    return wrapper