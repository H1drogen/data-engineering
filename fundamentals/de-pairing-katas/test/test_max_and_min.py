from src.max_and_min import nc_max, nc_min


def test_returns_numerical_value_when_given_list():
    List = [1,2,3,4]
    answer1 = nc_max(List)
    answer2 = nc_min(List)

    assert type(answer1) == int
    assert type(answer2) == int

def test_nc_max_returns_highest_value_when_given_list():
    List = [1,5,3,5,6]
    answer1 = nc_max(List)

    assert answer1 == 6

def test_nc_min_returns_lowest_value_when_given_list():
    List = [1,5,3,5,-2]
    answer1 = nc_min(List)

    assert answer1 == -2

def test_returns_0_when_given_empty_list():
    List = []
    answer1 = nc_max(List)
    answer2 = nc_min(List)

    assert answer1 == 0
    assert answer2 == 0