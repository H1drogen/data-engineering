
class Queue():
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.__front = 1
        self.__back = 0
        self.__storage = {}

    def enqueue(self, item):
        self.__back += 1
        self.storage[self.__back] = item

    def dequeue(self):
        if self.storage != {}:
            self.storage.pop(self.__front)

    def get_quantity(self):
        return self.__back

    def is_empty(self):
        if self.storage == {}:
            return True
        return False

    def is_full(self):
        if self.__back == self.max_size:
            return True
        return False

    @property
    def get_back_count(self):
        return self.__back

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, values):
        if isinstance(values, dict):
            self.__storage = values
            self.__back = len(values)
        return
