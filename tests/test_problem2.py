from problems.problem2 import solve


def test_case_one():
    assert solve(323, 4) == 32


def test_case_two():
    assert solve(909090909, 50) == 3


def test_case_three():
    assert solve(131203, 9) == 130
