from problems.problem3 import solve
from tests.input_test_case import problem3_format_input


def test_case_one():
    person = problem3_format_input("tests/in1.txt")
    assert solve(person) == 2


def test_case_two():
    person = problem3_format_input("tests/in2.txt")
    assert solve(person) == 7


def test_case_three():
    person = problem3_format_input("tests/in3.txt")
    assert solve(person) == 10000
