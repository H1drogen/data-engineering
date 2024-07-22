

class NCMap():
    def __init__(self, function, lst):
        self.function = function
        self.index = 0
        self.list = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        self.index += 1
        return self.function(self.list[self.index - 1])

