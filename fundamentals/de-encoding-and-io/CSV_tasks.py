import csv


def list_of_dictionaries(file_path: str):
    with open(file_path, 'rt') as f:
        file = csv.reader(f)
        output = []
        headers = next(file)
        for row in file:
            dictionary = {}
            for index, key in enumerate(headers):
                dictionary[key] = row[index]
            output.append(dictionary)
        return output

# list_of_dictionaries('./data/pizza.csv')

def pizza_ingredients(file_path, pizza):
    with open(file_path, 'rt') as f:
        file = csv.reader(f)
        name_index = 0
        ingredient_index = 0
        headers = next(file)
        for index, header in enumerate(headers):
            if header == 'Pizza':
                name_index = index
            if header == 'Description':
                ingredient_index = index
        for row in file:
            if row[name_index] == pizza:
                return row[ingredient_index].split(',')

# pizza_ingredients('./data/pizza.csv', 'Capri')

def pizza_under_value(file_path, value: float):
    with open(file_path, 'rt') as f:
        file = csv.reader(f)
        name_index = 0
        price_index = 0
        output = []
        headers = next(file)
        for index, header in enumerate(headers):
            if header == 'Pizza':
                name_index = index
            if header == 'Cost':
                price_index = index
        for row in file:
            if float(row[price_index][1:]) <= value:
                output.append([row[name_index], row[price_index]])
        return output.sort(key=lambda output: output[1][1:])

# pizza_under_value('./data/pizza.csv', 9)

def new_pizza(file_path, pizza):
    with open(file_path, 'a') as f:
        f.write(f'\n{pizza}')

# new_pizza('./data/pizza.csv', 'Sorrento,£9.00,"Mozzarella cheese, tomato, ham and pineapple",876kcal')

def increase_cost(file_path, percentage_change):
    with open(file_path, 'r+') as f:
        file = csv.DictWriter(f, fieldnames=f.__iter__())
        price_index = 0
        headers = next(file)
        for index, header in enumerate(headers):
            if header == 'Cost':
                price_index = index
        for row in file:
            inflated_value = float(row[price_index][1:]) * percentage_change
            row[price_index] = f'£{round(inflated_value, 2)}'
            f.write(','.join(row))
        return

increase_cost('./data/pizza.csv', 1.1)


