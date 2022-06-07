def problem3_format_input(path):
    with open(path) as file:
        person = []
        for line in file:
            numbers = line.split(" ")
            person.append((int(numbers[0]), int(numbers[1])))

        return person
