def once(func):
    count=0
    def check_once_only():
        nonlocal count
        if count<1:
            count+=1
            return func()
        else:
            return None
    return check_once_only