import pytest

from search import binary_search, linear_search


def test_linear_search_finds_value():
    numbers = [3, 7, 12, 18, 25]

    assert linear_search(numbers, 12) == 2


def test_linear_search_returns_minus_one_when_missing():
    numbers = [3, 7, 12, 18, 25]

    assert linear_search(numbers, 10) == -1


def test_linear_search_handles_empty_list():
    assert linear_search([], 10) == -1


def test_linear_search_handles_one_element_list():
    assert linear_search([10], 10) == 0
    assert linear_search([10], 5) == -1


def test_linear_search_finds_first_duplicate():
    numbers = [3, 7, 7, 12]

    assert linear_search(numbers, 7) == 1


def test_binary_search_finds_value():
    numbers = [3, 7, 12, 18, 25]

    assert binary_search(numbers, 18) == 3


def test_binary_search_returns_minus_one_when_missing():
    numbers = [3, 7, 12, 18, 25]

    assert binary_search(numbers, 10) == -1


def test_binary_search_handles_empty_list():
    assert binary_search([], 10) == -1


def test_binary_search_handles_one_element_list():
    assert binary_search([10], 10) == 0
    assert binary_search([10], 5) == -1


def test_binary_search_finds_first_or_any_duplicate():
    numbers = [3, 7, 7, 12]

    assert binary_search(numbers, 7) in [1, 2]


def test_binary_search_rejects_unsorted_list():
    numbers = [18, 3, 25, 7, 12]

    with pytest.raises(ValueError):
        binary_search(numbers, 18)