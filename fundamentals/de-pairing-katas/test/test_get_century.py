from src.get_century import get_century

# The function get_century should take a year as a number and return the century as a string.
# It should work up to and including the year 9,999 (the '100th' century).

def test_string_is_returned():
    year = 2024
    answer1 = get_century(year)
   
    assert type(answer1) is str

def test_string_():
    year1 = 1999
    answer1 = get_century(year1)
    expected1="20th"
    year2 = 2004
    answer2 = get_century(year2)
    expected2="21st"
    year3 = 1877
    answer3 = get_century(year3)
    expected3="19th"

   
    assert answer1 == expected1
    assert answer2 == expected2
    assert answer3 == expected3


