from collections import defaultdict


def add(inputs, param1, param2, param3):
    result = param1 + param2
    inputs[param3] = result


def multiply(inputs, param1, param2, param3):
    result = param1 * param2
    inputs[param3] = result


def echoValue(inputs, value):
    print("Echoed: {}".format(value))
    return value


def jumpIfTrue(param1):
    return param1 != 0


def jumpIfFalse(param1):
    return param1 == 0


def lessThan(values, param1, param2, param3):
    result = 1 if param1 < param2 else 0
    values[param3] = result


def equal(values, param1, param2, param3):
    result = 1 if param1 == param2 else 0
    values[param3] = result


def addPaddingToOpCode(opCode):
    string = str(opCode)
    return "0" * (5 - len(string)) + string


def getParam(inputs, paramMode, value, relativeOffset):
    if paramMode == 0:
        return inputs[value]
    elif paramMode == 1:
        return value
    elif paramMode == 2:
        return inputs[value + relativeOffset]


def getParams(inputs, instruction, i, relativeOffset=0):
    modes = instruction[:-2]
    opCode = int(instruction[-2:])
    param1Mode = int(modes[-1])
    param2Mode = int(modes[-2])
    param3Mode = int(modes[-3])

    if opCode == 99:
        return opCode, False, False, False

    if opCode <= 2 or opCode == 7 or opCode == 8:
        param1 = getParam(inputs, param1Mode, inputs[i + 1], relativeOffset)
        param2 = getParam(inputs, param2Mode, inputs[i + 2], relativeOffset)
        param3 = inputs[i + 3] if param3Mode == 0 else inputs[i + 3] + relativeOffset

        return opCode, param1, param2, param3
    elif opCode == 3:
        param1 = inputs[i + 1] if param1Mode == 0 else inputs[i + 1] + relativeOffset

        return opCode, param1, False, False
    elif opCode == 4 or opCode == 9:
        param1 = getParam(inputs, param1Mode, inputs[i + 1], relativeOffset)

        return opCode, param1, False, False
    elif opCode == 5 or opCode == 6:
        param1 = getParam(inputs, param1Mode, inputs[i + 1], relativeOffset)
        param2 = getParam(inputs, param2Mode, inputs[i + 2], relativeOffset)
        return opCode, param1, param2, False


def intCodeProgram(inputs, args, startIndex=0, haltAtOutput=False):
    values = defaultdict(int)
    for i in range(len(inputs)):
        values[i] = inputs[i]

    i = startIndex
    argIndex = 0
    lastEchoed = 0
    relativeBase = 0
    while True:
        instruction = addPaddingToOpCode(values[i])
        opCode = int(instruction[-1])
        opCode, param1, param2, param3 = getParams(values, instruction, i, relativeBase)

        if opCode == 99:
            return -1, lastEchoed, values
        if opCode == 1:
            add(values, param1, param2, param3)
            i += 4
        elif opCode == 2:
            multiply(values, param1, param2, param3)
            i += 4
        elif opCode == 3:
            inputValue = args[argIndex]
            values[param1] = inputValue
            argIndex = (argIndex + 1) % len(args)
            i += 2
        elif opCode == 4:
            lastEchoed = echoValue(values, param1)
            i += 2
            if haltAtOutput:
                return i, lastEchoed, values
        elif opCode == 5:
            shouldJump = jumpIfTrue(param1)
            if shouldJump:
                i = param2
            else:
                i += 3
        elif opCode == 6:
            shouldJump = jumpIfFalse(param1)
            if shouldJump:
                i = param2
            else:
                i += 3
        elif opCode == 7:
            lessThan(values, param1, param2, param3)
            i += 4
        elif opCode == 8:
            equal(values, param1, param2, param3)
            i += 4
        elif opCode == 9:
            relativeBase += param1
            i += 2


def part1(inputs):
    _, output, _ = intCodeProgram(inputs, [1])

    return "BOOST keycode: {}".format(output)


def part2(inputs):
    _, output, _ = intCodeProgram(inputs, [2])

    return "Distress signal coordinates: {}".format(output)
