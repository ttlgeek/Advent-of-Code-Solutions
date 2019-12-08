def add(inputs, param1, param2, param3):
    result = param1 + param2
    inputs[param3] = result


def multiply(inputs, param1, param2, param3):
    result = param1 * param2
    inputs[param3] = result


def echoValue(inputs, index):
    return inputs[index]


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


def intCodeProgram(inputs, args, startIndex=0, haltAtOutput=False):
    values = [i for i in inputs]
    i = startIndex
    argIndex = 0
    lastEchoed = 0
    while True:
        instruction = addPaddingToOpCode(values[i])
        opCode = int(instruction[-1])
        opCode, param1, param2, param3 = getParams(values, instruction, i)
        if opCode == 99:
            return -1, lastEchoed, values
        if opCode == 1:
            add(values, param1, param2, param3)
            i += 4
        elif opCode == 2:
            multiply(values, param1, param2, param3)
            i += 4
        elif opCode == 3:
            values[param1] = args[argIndex]
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


def getNextPhaseSettings(phaseSettings):
    i = 4
    nextPhaseSettings = [i for i in phaseSettings]
    while i >= 0:
        if nextPhaseSettings[i] < 4:
            nextPhaseSettings[i] += 1
            break
        nextPhaseSettings[i] = 0
        i -= 1

    if len(list(set(nextPhaseSettings))) < len(nextPhaseSettings):
        return getNextPhaseSettings(nextPhaseSettings)
    return nextPhaseSettings


def getNextFeedbackPhaseSettings(phaseSettings):
    i = 4
    nextPhaseSettings = [i for i in phaseSettings]
    while i >= 0:
        if nextPhaseSettings[i] < 9:
            nextPhaseSettings[i] += 1
            break
        nextPhaseSettings[i] = 5
        i -= 1

    if len(list(set(nextPhaseSettings))) < len(nextPhaseSettings):
        return getNextFeedbackPhaseSettings(nextPhaseSettings)
    return nextPhaseSettings


def part1(inputs):
    maxOutput = 0
    phaseSettings = initialPhaseSettings = [0, 1, 2, 3, 4]

    phaseSettings = getNextPhaseSettings(phaseSettings)
    while phaseSettings != initialPhaseSettings:
        values = [i for i in inputs]
        thrusterOutputs = [intCodeProgram(values, [phaseSettings[0], 0])[1]]
        for i in range(1, 5):
            lastIndex, output, state = intCodeProgram(
                values, [phaseSettings[i], thrusterOutputs[i - 1]]
            )
            thrusterOutputs.append(output)
        maxOutput = max(maxOutput, thrusterOutputs[-1])
        phaseSettings = getNextPhaseSettings(phaseSettings)
    return maxOutput


def part2(inputs):
    phaseSettings = initialPhaseSettings = [5, 6, 7, 8, 9]

    maxOutput = 0

    phaseSettings = getNextFeedbackPhaseSettings(phaseSettings)
    while phaseSettings != initialPhaseSettings:
        ampIndex = 0
        passedFirstLoop = False
        states = {i: ([i for i in inputs], 0, 0) for i in range(5)}
        lastIndex, output, state = intCodeProgram(
            inputs, [phaseSettings[ampIndex], 0], 0, True
        )
        states[0] = state, lastIndex, output
        ampIndex = 1
        while True:
            lastState, lastIndex, _ = states[ampIndex]
            args = (
                [
                    phaseSettings[ampIndex],
                    states[ampIndex - 1 if ampIndex != 0 else 4][2],
                ]
                if not passedFirstLoop
                else [states[ampIndex - 1 if ampIndex != 0 else 4][2]]
            )
            lastIndex, output, state = intCodeProgram(lastState, args, lastIndex, True)

            if lastIndex == -1:
                break

            states[ampIndex] = state, lastIndex, output
            if ampIndex + 1 == 5:
                passedFirstLoop = True
            ampIndex = (ampIndex + 1) % 5
        maxOutput = max(maxOutput, states[4][2])
        phaseSettings = getNextFeedbackPhaseSettings(phaseSettings)
        ampIndex = 0

    return maxOutput
