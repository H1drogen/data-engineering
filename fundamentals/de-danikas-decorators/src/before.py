def before(num):
    def before_decorator(func):
        count=0
        def wrapper():
            nonlocal count
            count+=1
            if count<num:
                return (func())
        return wrapper
    return before_decorator