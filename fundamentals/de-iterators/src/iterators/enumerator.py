class NCEnumerate():
    # implement me
    def __init__(self, lst):
        self.list = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        self.index += 1
        return (self.index - 1), self.list[self.index - 1]




