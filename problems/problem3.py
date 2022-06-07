def solve(students):
    hours = []

    for arrival, depart in students:
        hours.append((arrival, 1))
        hours.append((depart, -1))

    hours.sort()
    answer = 0
    current = 0

    for h in hours:
        current += h[1]
        answer = max(answer, current)

    return answer
