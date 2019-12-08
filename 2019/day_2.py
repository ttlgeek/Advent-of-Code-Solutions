def part1(inputs):
    values = [i for i in inputs]
    for i in range(0, len(values), 4):
        opCode = values[i]
        if opCode == 99:
            return values[0]
        param1 = values[values[i + 1]]
        param2 = values[values[i + 2]]
        param3 = values[i + 3]
        if opCode == 1:
            add(values, param1, param2, param3)
        elif opCode == 2:
            multiply(values, param1, param2, param3)
        else:
            return values[0]


def add(inputs, param1, param2, param3):
    result = param1 + param2
    inputs[param3] = result


def multiply(inputs, param1, param2, param3):
    result = param1 * param2
    inputs[param3] = result


def part2(inputs):
    values = [i for i in inputs]
    x = 0
    y = 0
    for i in range(100):
        x = i
        for k in range(100):
            y = k
            values[1] = x
            values[2] = y
            result = part1(values)
            if result == 19690720:
                return 100 * x + y
