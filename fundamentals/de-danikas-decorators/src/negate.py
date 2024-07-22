def negate(func):
    def negated_func():
        output=func()
        return not output

    return negated_func
