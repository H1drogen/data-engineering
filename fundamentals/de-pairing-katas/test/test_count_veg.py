from src.count_veg import count_veg



# The function count_veg should take a list of vegetables and a string of the type of vegetable. 
# It should return the total quantity of that type of vegetable in the list.

# Vegetable types can be root, leaf, legume, bulb or brassica.

def test_single_dictionary_item():
    test1 = [{"name": 'Parsnip', "type": 'root', "quantity": 4}]
    veg_type = 'root'

    answer1 = count_veg(test1, veg_type)
   
    assert answer1 == 4

#test 2
def test_multiple_dictionary_item():
    test1 = [
  {"name": 'Parsnip', "type": 'root', "quantity": 4},
  {"name": 'Broccoli', "type": 'brassica', "quantity": 1},
  {"name": 'Carrot', "type": 'root', "quantity": 5},
  {"name": 'Onion', "type": 'bulb', "quantity": 3},
  {"name": 'Chard', "type": 'leaf', "quantity": 3},
  {"name": 'Runner beans', "type": 'legume', "quantity": 8}]
    veg_type = 'root'

    answer1 = count_veg(test1, veg_type)
   
    assert answer1 == 9


def test_multiple_dictionary_item_returns_0():
    test1 = [
        {"name": 'Parsnip', "type": 'root', "quantity": 4},
        {"name": 'Broccoli', "type": 'brassica', "quantity": 1},
        {"name": 'Carrot', "type": 'root', "quantity": 5},
        {"name": 'Onion', "type": 'bulb', "quantity": 3},
        {"name": 'Chard', "type": 'leaf', "quantity": 3},
        {"name": 'Runner beans', "type": 'legume', "quantity": 8}]
    veg_type = 'fruit'

    answer1 = count_veg(test1, veg_type)

    assert answer1 == 0

