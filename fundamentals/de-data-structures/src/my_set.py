
class set():
    def __init__(self, values = []):
        self.storage = values

    def add(self, element):
        for item in self.storage:
            if item == element:
                return
        self.storage.append(element)

    def remove(self, element):
        for item in self.storage:
            if item == element:
                self.storage.remove(item)
                return
        return



