def fib(n):
    count = 0
    current = 1
    prev = 0
    while count < n:
        current = current + prev
        prev = current - prev
        count += 1
        yield current
