def solve(number, iterations):
    while iterations > 0:
        if not number % 10:
            number //= 10
        else:
            number -= 1

        iterations -= 1

    return number
