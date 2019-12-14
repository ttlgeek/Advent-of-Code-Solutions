from day_9 import intCodeProgram


def part1(program):
    _, output, _, _ = intCodeProgram(program, [])
    result = 0
    for i in range(0, len(output), 3):
        x, y, tileId = output[i : i + 3]
        if tileId == 2:
            result += 1

    return result
