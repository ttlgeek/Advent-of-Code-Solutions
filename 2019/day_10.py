from collections import defaultdict


def lineFromPoints(P, Q):

    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])

    # ax + by = c
    return a, b, c


def pointBelongsToLine(P, a, b, c):
    return a * P[0] + b * P[1] == c


def getVector(vectorBase, vectorHead):
    return (
        vectorHead[0] - vectorBase[0],
        vectorHead[1] - vectorBase[1],
    )


def vectorsAreFacingSameDirection(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] + vector2[1] > 0


def convertToCoordinates(mapArr):
    coordinatesDict = dict()

    for i in range(len(mapArr)):
        row = mapArr[i]
        for k in range(len(row)):
            coordinatesDict[(k, i)] = row[k]

    return [k for k, v in coordinatesDict.items() if v == "#"], coordinatesDict


#       ,---------------- x=[0, W - 1], y = 0 ---------------,
#       |                                                    |
#       |                                                    |
#       |                                                    |
#       |                                                    |
#       |                         X                          |
# x=0, y = [0, H - 1]                                 x=W - 1, y = [0, H - 1]
#       |                                                    |
#       |                                                    |
#       |                                                    |
#       '_________________x=[0, W - 1], y = H________________'


def getBeamHeadPositions(stationCoordinates, W, H):
    startPoint = (stationCoordinates[0], 0)
    positions = [startPoint]
    lastPoint = startPoint
    while positions[-1][0] < W - 1:
        lastPoint = positions[-1]
        lastPoint = (lastPoint[0] + 1, lastPoint[1])
        positions.append(lastPoint)
    while positions[-1][1] < H - 1:
        lastPoint = positions[-1]
        lastPoint = (lastPoint[0], lastPoint[1] + 1)
        positions.append(lastPoint)
    while positions[-1][0] > 0:
        lastPoint = positions[-1]
        lastPoint = (lastPoint[0] - 1, lastPoint[1])
        positions.append(lastPoint)
    while positions[-1][1] > 0:
        lastPoint = positions[-1]
        lastPoint = (lastPoint[0], lastPoint[1] - 1)
        positions.append(lastPoint)
    while lastPoint != startPoint:
        lastPoint = positions[-1]
        lastPoint = (lastPoint[0] + 1, lastPoint[1])
        positions.append(lastPoint)
    return positions[:-1]


def hasPointInBetween(coordinates, firstPoint, secondPoint):
    a, b, c = lineFromPoints(firstPoint, secondPoint)

    for i in coordinates:
        if i == firstPoint or i == secondPoint:
            continue
        # print(i, pointBelongsToLine(i, a, b, c))

        if pointBelongsToLine(i, a, b, c):
            manhattan1 = abs(firstPoint[0] - i[0]) + abs(firstPoint[1] - i[1])
            manhattan2 = abs(secondPoint[0] - i[0]) + abs(secondPoint[1] - i[1])
            bigManhattan = abs(secondPoint[0] - firstPoint[0]) + abs(
                secondPoint[1] - firstPoint[1]
            )

            condition = manhattan1 + manhattan2 == bigManhattan
            if condition:
                # print("\tIs between points, should not be counted")
                return True
            else:
                pass
                # print("\tIs not between points")
    return False


def part1(mapArr):
    coordinates, _ = convertToCoordinates(mapArr)
    visibleAstroidsCount = defaultdict(int)
    for firstPoint in coordinates:
        for secondPoint in coordinates:
            if firstPoint == secondPoint:
                continue
            # print("First point: {}, Second point: {}".format(firstPoint, secondPoint))

            if not hasPointInBetween(coordinates, firstPoint, secondPoint):
                visibleAstroidsCount[firstPoint] += 1

    maxVisible = max(visibleAstroidsCount.values())

    return (
        [
            k
            for k, v in visibleAstroidsCount.items()
            if v == max(visibleAstroidsCount.values())
        ][0],
        maxVisible,
    )


"""
def part2(mapArr):
    stationCoordinates, _ = part1(mapArr)
    coordinates, coordinatesMap = convertToCoordinates(mapArr)

    vaporizedCount = 0

    beamHeadPositions = getBeamHeadPositions(
        stationCoordinates, len(mapArr[0]), len(mapArr)
    )

    for position in beamHeadPositions:
        a, b, c = lineFromPoints(stationCoordinates, position)
        # print("Point 1: ", stationCoordinates, "Point 2: ", position)
        beamVector = getVector(stationCoordinates, position)
        # print("Vector: ", beamVector)

        for point in coordinates:
            if coordinatesMap[point] == "#":
                pointVector = getVector(stationCoordinates, point)

                if pointBelongsToLine(position, a, b, c):
                    if not hasPointInBetween(
                        coordinates, stationCoordinates, point
                    ) and vectorsAreFacingSameDirection(beamVector, pointVector):
                        print(stationCoordinates, point)
                        coordinatesMap[point] = "."
                        vaporizedCount += 1
                        if vaporizedCount == 200:
                            return point
        coordinates = [k for k, v in coordinatesMap.items() if v == "#"]
    print(vaporizedCount)
"""
