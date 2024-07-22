from src.sum_args import sum_args

# The function sum_args should accept any number of arguments and add them together.

def test_add_three_args():
    a=1
    b=2
    c=3

    answer1 = sum_args(a,b,c)
   
    assert answer1==6

def test_add_three_args_with_one_zero():
    a=0
    b=2
    c=3

    answer1 = sum_args(a,b,c)
   
    assert answer1==5

# If given one argument, it should return that. 
def test_given_1_arg():
    a=5
    answer1 = sum_args(a)
   
    assert answer1==5

# If it is not given arguments, it should return 0.

def test_given_0_arg():
    answer1 = sum_args()
   
    assert answer1==0
