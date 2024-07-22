# Implement your stack here

class Stack():
    def __init__(self, max_size=100):
        self.quantity = 0
        self.storage = {}
        self.max_size = max_size

    def push(self, item):
        self.quantity += 1
        self.storage[self.quantity] = item

    def pop(self):
        if self.quantity > 0:
            self.quantity -= 1
            return self.storage.pop(self.quantity + 1)
        return

    def is_empty(self):
        if self.quantity == 0 and self.storage == {}:
            return True
        return False

    def is_full(self):
        if self.quantity == self.max_size:
            return True
        return False

    def peek(self):
        return self.storage.get(self.quantity)
