from src.check_usernames import check_usernames

# The function check_usernames should take an list of usernames and return True if they are all valid. If any are not valid, it should return False.
# A valid username:

# is at least 5 characters long

def test_5_char_long_is_true():
    user_name1 = '12345'
    answer1 = check_usernames(user_name1)   
    assert answer1==True

def test_4_char_long_is_false():
    user_name2 = '1234'
    answer2 = check_usernames(user_name2)   
    assert answer2==False

def test_6_char_long_is_false():
    user_name3 = '123456'
    answer3 = check_usernames(user_name3)   
    assert answer3==True

# may only contain lowercase letters, numbers and underscores
def test_contains_unallowable_char_false():
    user_name4 = 'HELLO'
    answer4 = check_usernames(user_name4)   
    assert answer4==False

def test_contains_unallowable_char_false_v2():
    user_name5 = 'hE!*0'
    answer5 = check_usernames(user_name5)   
    assert answer5==False

# is no longer than 20 characters

def test_is_21_char_false():
    user_name6 = '123456789123456789012345'
    answer6 = check_usernames(user_name6)   
    assert answer6==False

def test_is_20_char_True():
    user_name7 = 'asdfghjkl123456789_a'
    answer7 = check_usernames(user_name7)   
    assert answer7==True

