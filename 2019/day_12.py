from collections import OrderedDict
from copy import deepcopy
from itertools import combinations


def extractCoordinates(stringArr):
    moons = []
    for i in stringArr:
        moonCoordinates = []
        split_string = i.split(", ")
        for i in split_string:
            i = i.replace(">", "")
            equalsIndex = i.index("=")
            moonCoordinates.append(int(i[equalsIndex + 1 :]))
        moons.append(tuple(moonCoordinates))

    return moons


def printStatus(data):
    for moon, velocity in data.items():
        print(
            f"pos=<x=  {moon[0]}, y=  {moon[1]}, z=  {moon[2]}>, vel=<x=  {velocity[0]}, y=  {velocity[1]}, z=  {velocity[2]}>"
        )
    print()


def updateVelocities(data):
    newVelocities = deepcopy(data)
    for pair in combinations(newVelocities.keys(), 2):
        moon1 = pair[0]
        moon2 = pair[1]

        moon1Velocity = newVelocities[moon1]
        moon2Velocity = newVelocities[moon2]

        for p in range(3):
            if moon1[p] > moon2[p]:
                moon1Velocity[p] -= 1
                moon2Velocity[p] += 1
            elif moon1[p] < moon2[p]:
                moon2Velocity[p] -= 1
                moon1Velocity[p] += 1

        newVelocities[moon1] = moon1Velocity
        newVelocities[moon2] = moon2Velocity
    return newVelocities


def updateMoonPositions(data):
    newVelocities = OrderedDict()
    for moon, velocity in data.items():
        newMoon = list(moon)
        for p in range(3):
            newMoon[p] += velocity[p]
        newVelocities[tuple(newMoon)] = velocity

    return newVelocities


def computeTotalEnergy(data):
    result = 0
    for k, v in data.items():
        pot = sum([abs(i) for i in list(k)])
        kin = sum([abs(i) for i in v])

        result += pot * kin

    return result


def part1(stringArr):
    moons = extractCoordinates(stringArr)
    data = {moon: [0, 0, 0] for moon in moons}

    print("After 0 steps:")
    printStatus(data)
    for step in range(1000):
        data = updateVelocities(data)

        data = updateMoonPositions(data)

    print("After 1000 steps:")
    printStatus(data)

    result = computeTotalEnergy(data)

    return f"Total energy in the system: {result}"


"""
def stateExistedOnce(data, universeHistory):
    for state in universeHistory:
        if state == data:
            return True
    return False


def part2(stringArr):
    # DOESN'T PRODUCE OUTPUT
    moons = extractCoordinates(stringArr)
    data = {moon: [0, 0, 0] for moon in moons}

    steps = 0
    universeHistory = [data]

    while True:
        steps += 1

        data = updateVelocities(data)

        data = updateMoonPositions(data)

        if stateExistedOnce(data, universeHistory):
            return steps
"""
