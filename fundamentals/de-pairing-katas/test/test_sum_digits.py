from src.sum_digits import sum_digits



# Tests for sum_digits

# TEST 1 - sum_digits returns the input number when passed a single digit number
# This test has two ASSERTIONS being made
# The same behaviour is being tested but with different inputs - 1 and 9

def test_sum_digits_returns_input_when_passed_single_digit():
    test1 = 1
    test2 = 9

    answer1 = sum_digits(test1)
    answer2 = sum_digits(test2)

    assert answer1 == 1
    assert answer2 == 9


# E.g. sum_digits(1) should output 1
# E.g. sum_digits(9) should output 9


# Once you have got the first test passing, then you can write your next one.
# If you've already handled a single digit, your next test could test for multi-digit inputs.

# E.g. sum_digits(99) should output 18
# E.g. sum_digits(123) should output 6

def test_sum_digits_returns_input_when_passed_multiple_digits():
    test1 = 13
    test2 = 923

    answer1 = sum_digits(test1)
    answer2 = sum_digits(test2)

    assert answer1 == 4
    assert answer2 == 14

# HINT: Remember to see the test *fail* first, then write the code to pass the test

# Why this test?
# A multi-digit input means you now have to implement to 'addition' part of this function,
# but you don't have to think about the logic for dealing with/ignoring non-digit characters yet
# (that's for our next test!)

def test_sum_digits_returns_input_when_passed_with_non_digits():
    test1 = 1.3
    test2 = 92.3

    answer1 = sum_digits(test1)
    answer2 = sum_digits(test2)

    assert answer1 == 4
    assert answer2 == 14


# Once you have successfully passed the above test, then you can write your next test.
# A good next test might be to check that your function handles non-numerical characters correctly (i.e. ignores them)

# E.g. sum_digits(10.5) should output 6
