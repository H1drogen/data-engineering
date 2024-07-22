from src.are_ordered import are_ordered

# The are_ordered function should take a list of numbers as an input. 
# It should return True if all the numbers are in ascending order and False if they are not. 
# An empty list should also return False.

def test_ordered_list_should_be_true():
    list1 = [1,2,3,4,5]
    answer1 = are_ordered(list1)
   
    assert answer1==True

def test_ordered_list_should_be_false():
    list1 = [5,2,3,4,1]
    answer1 = are_ordered(list1)
   
    assert answer1==False

def test_empty_list_should_be_false():
    list1 = []
    answer1 = are_ordered(list1)
   
    assert answer1==False