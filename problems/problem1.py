def solve(brackets):
    count = 0

    open_brackets = {'{', '[', '('}

    for b in brackets:
        if b in open_brackets:
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return True
