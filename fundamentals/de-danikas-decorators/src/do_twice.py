def do_twice(func):
    count=0
    def twicer():
        nonlocal count
        count+=1
        func()
        count+=1
        func()
        if count==2:
            return True

    return twicer