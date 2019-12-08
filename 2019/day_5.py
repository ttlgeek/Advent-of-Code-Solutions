def add(inputs, param1, param2, param3):
    result = param1 + param2
    inputs[param3] = result


def multiply(inputs, param1, param2, param3):
    result = param1 * param2
    inputs[param3] = result


def takeAndStoreInput(inputs, index):
    number = input("Please provide a number: ")
    inputs[index] = int(number)


def echoValue(inputs, index):
    print("Echoed: {}\n ".format(inputs[index]))


def jumpIfTrue(param1):
    return param1 != 0


def jumpIfFalse(param1):
    return param1 == 0


def lessThan(values, param1, param2, param3):
    values[param3] = 1 if param1 < param2 else 0


def equal(values, param1, param2, param3):
    values[param3] = 1 if param1 == param2 else 0


def addPaddingToOpCode(opCode):
    string = str(opCode)
    return "0" * (4 - len(string)) + string


def getParams(inputs, instruction, i):
    modes = instruction[:-2]
    opCode = int(instruction[-2:])
    param1Mode = int(modes[-1])
    param2Mode = int(modes[-2])

    if opCode == 99:
        return opCode, False, False, False

    if opCode <= 2 or opCode == 7 or opCode == 8:
        param1 = inputs[inputs[i + 1]] if param1Mode == 0 else inputs[i + 1]
        param2 = inputs[inputs[i + 2]] if param2Mode == 0 else inputs[i + 2]
        param3 = inputs[i + 3]
        return opCode, param1, param2, param3
    elif opCode == 3:
        param1 = inputs[i + 1]
        return opCode, param1, False, False
    elif opCode == 4:
        param1 = inputs[i + 1] if param1Mode == 0 else i + 1
        return opCode, param1, False, False
    elif opCode == 5 or opCode == 6:
        param1 = inputs[inputs[i + 1]] if param1Mode == 0 else inputs[i + 1]
        param2 = inputs[inputs[i + 2]] if param2Mode == 0 else inputs[i + 2]
        return opCode, param1, param2, False


def part1(inputs):
    values = [i for i in inputs]
    i = 0

    while True:
        instruction = addPaddingToOpCode(values[i])
        opCode, param1, param2, param3 = getParams(values, instruction, i)
        if opCode == 99:
            return values[0]
        print(
            "Instruction: {}, param1: {}, param2: {}, storePosition: {}\nArr: {}\n".format(
                instruction, param1, param2, param3, values[i : i + 4]
            )
        )
        if opCode == 1:
            add(values, param1, param2, param3)
            i += 4
        elif opCode == 2:
            multiply(values, param1, param2, param3)
            i += 4
        elif opCode == 3:
            takeAndStoreInput(values, param1)
            i += 2
        elif opCode == 4:
            echoValue(values, param1)
            i += 2


def part2(inputs):
    values = [i for i in inputs]
    i = 0

    while True:
        instruction = addPaddingToOpCode(values[i])
        opCode = int(instruction[-1])
        opCode, param1, param2, param3 = getParams(values, instruction, i)
        if opCode == 99:
            return values[0]
        print(
            "Instruction: {}, param1: {}, param2: {}, storePosition: {}\nArr: {}\n".format(
                instruction, param1, param2, param3, values[i : i + 4]
            )
        )
        if opCode == 1:
            add(values, param1, param2, param3)
            i += 4
        elif opCode == 2:
            multiply(values, param1, param2, param3)
            i += 4
        elif opCode == 3:
            takeAndStoreInput(values, param1)
            i += 2
        elif opCode == 4:
            echoValue(values, param1)
            i += 2
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
