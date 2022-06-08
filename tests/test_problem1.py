from problems.problem1 import solve


def test_case_one():
    brackets = "(())))((()()()()()))))"
    assert solve(brackets) is False


def test_case_two():
    brackets = "(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))"
    assert solve(brackets) is True


def test_case_three():
    brackets = "))))))))))(((((((((("
    assert solve(brackets) is False
