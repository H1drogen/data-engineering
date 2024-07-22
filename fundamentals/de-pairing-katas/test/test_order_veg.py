from src.order_veg import order_veg

# The order_veg function should take a list of vegetables and return a new list 
# in which the vegetables are sorted in ascending order according to quantity.

def test_empty_returns_empty():
    input = []
    answer1 = order_veg(input)
   
    assert answer1==[]


def test_2_item_list():
    input = [{"name": 'Parsnip', "type": 'root', "quantity": 4},
             {"name": 'Broccoli', "type": 'brassica', "quantity": 1}]
    answer1 = order_veg(input)
   
    assert answer1==[{"name": 'Broccoli', "type": 'brassica', "quantity": 1}, 
                     {"name": 'Parsnip', "type": 'root', "quantity": 4}]
