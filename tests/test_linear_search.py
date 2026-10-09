from examples.linear_search import linear_search


def test_finds_first_match() -> None:
    assert linear_search([4, 8, 8, 2], 8) == 1


def test_missing_value() -> None:
    assert linear_search([4, 8, 2], 10) == -1


def test_empty_list() -> None:
    assert linear_search([], 10) == -1


def test_negative_numbers() -> None:
    assert linear_search([-2, -5, 3], -5) == 1
