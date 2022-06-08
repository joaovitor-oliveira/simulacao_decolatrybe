def solve(brackets):
    count = 0

    for b in brackets:
        if b == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0
