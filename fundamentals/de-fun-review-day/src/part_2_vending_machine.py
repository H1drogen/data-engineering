class VendingMachine:

    def __init__(self):
        self.credit = 0
        self.stock = {'A': {}, 'B': {}, 'C': {}}

    def add_credit(self, amount):
        self.credit += amount

    def credit_checker(self, price):
        if self.credit < price:
            return False
        return True

    def add_stock(self, item, position):
        self.stock[position] = item

    def purchase_item(self, name):
        for item in self.stock.values():
            if name == item.get('name'):
                if self.credit_checker(item.get('price')):
                    item['quantity'] -= 1
                    return item.get('name')
                else:
                    return 'Insufficient credit!'