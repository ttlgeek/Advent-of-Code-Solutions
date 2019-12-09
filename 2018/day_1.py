def getNumber(frequencyChange):
    sign = frequencyChange[0]
    number = int(frequencyChange[1:])
    return number if sign == "+" else -number


def part1(frequencyChanges):
    result = 0
    for frequencyChange in frequencyChanges:
        result += getNumber(frequencyChange)

    return result


def part2(frequencyChanges):
    frequency = 0
    frequencyCache = {0: True}
    while True:
        for frequencyChange in frequencyChanges:
            frequency += getNumber(frequencyChange)
            if frequency in frequencyCache:
                return frequency
            else:
                frequencyCache[frequency] = True
