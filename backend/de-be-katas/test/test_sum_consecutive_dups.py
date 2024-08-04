from src.sum_consecutive_duplicates import sum_consecutive_duplicates, reduce_consecutive_duplicates


def test_sum_consecutive_duplicates_returns_unduplicated_list_passed_in():
    assert sum_consecutive_duplicates([1, 2, 3]) == [1, 2, 3]

def test_sum_consecutive_duplicates_returns_unduplicated_list_passed_in_with_duplicates():
    assert sum_consecutive_duplicates([1, 1, 2, 3]) == [2, 2, 3]

def test_sum_consecutive_duplicates_works_passed_in_with_many_duplicates():
    assert sum_consecutive_duplicates([1, 1, 2, 2, 3, 3]) == [2, 4, 6]

def test_sum_consecutive_duplicates_works_passed_in_with_unstructured_duplicates():
    assert sum_consecutive_duplicates([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [2, 2, 4, 2, 3]

def test_reduce_consecutive_duplicates_returns_unduplicated_list_passed_in():
    assert reduce_consecutive_duplicates([1, 2, 3]) == [1, 2, 3]

def test_reduce_consecutive_duplicates_returns_unduplicated_list_passed_in_with_duplicates():
    assert reduce_consecutive_duplicates([1, 1, 2, 3]) == [4, 3]

def test_reduce_consecutive_duplicates_works_passed_in_with_more_duplicates():
    assert reduce_consecutive_duplicates([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [8, 2, 3]


