from src.get_years_of_growth import get_years_of_growth

# The function get_years_of_growth should take 4 parameters: 
# a starting population, an end population, a percentage of growth and a net migration figure.

# If the population grows by the given percentage each year, 

def test_only_percentage():
    start_pop=10
    end_pop=11
    percentage=10
    migration=0
    answer = get_years_of_growth(start_pop,end_pop,percentage,migration)

    assert answer == 1

def test_only_percentage_v2():
    start_pop=10
    end_pop=15
    percentage=10
    migration=0
    answer = get_years_of_growth(start_pop,end_pop,percentage,migration)

    assert answer == 5

# plus an additional number of net migrants, 
def test_migration_and_growth():
    start_pop=10
    end_pop=12
    percentage=10
    migration=1
    answer = get_years_of_growth(start_pop,end_pop,percentage,migration)

    assert answer == 1

def test_migration_and_growth_v2():
    start_pop=10
    end_pop=15
    percentage=10
    migration=1
    answer = get_years_of_growth(start_pop,end_pop,percentage,migration)

    assert answer == 3

# the function should calculate how many years it takes until the end population total is reached.







