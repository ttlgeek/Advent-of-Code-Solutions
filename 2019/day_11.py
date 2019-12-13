from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from day_9 import intCodeProgram


def moveRobot(currentDirectionIndex, directionChanger, coordinates):
    directions = ["U", "R", "D", "L"]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = coordinates

    nextDirection = currentDirectionIndex

    if directionChanger == 0:
        nextDirection = (currentDirectionIndex - 1 + 4) % 4
    elif directionChanger == 1:
        nextDirection = (currentDirectionIndex + 1) % 4

    return (nextDirection, x + dx[nextDirection], y + dy[nextDirection])


def calculateRobotPath(inputs, startingPanelColor=0):
    values = list.copy(inputs)
    panelColors = defaultdict(int)

    instructionIndex = 0
    relativeBase = 0
    args = [0]
    directionIndex = 0
    x = y = 0

    panelColors[(x, y)] = startingPanelColor

    painted = set()
    while True:
        instructionIndex, output, values, relativeBase = intCodeProgram(
            values,
            [panelColors[(x, y)]],
            instructionIndex,
            haltAtOutput=True,
            outputSize=2,
            startRelativeBase=relativeBase,
        )

        if instructionIndex == -1:
            break

        panelColor = output[0]
        turnDirection = output[1]

        panelColors[(x, y)] = panelColor
        painted.add((x, y))
        directionIndex, x, y = moveRobot(directionIndex, turnDirection, (x, y))

    return len(painted), panelColors


def part1(inputs):
    area, _ = calculateRobotPath(inputs)

    return f"Estimated area: {area}"
