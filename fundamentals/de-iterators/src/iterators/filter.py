class NCFilter:
    def __init__(self, function, example_list):
        self.function = function 
        self.example_list = example_list
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.function(self.example_list[self.count]):
            self.count += 1
        else: 
            del self.example_list[self.count]
        