from collections import defaultdict

def part1(wire1Path, wire2Path):
  coordinatesCount1 = calculatePath(wire1Path)
  coordinatesCount2 = calculatePath(wire2Path)
  duplicates = [k for k,v in coordinatesCount1.items() if k in coordinatesCount2]
  manhattanDistances = [sum([abs(int(v)) for v in k.split(", ")]) for k in duplicates]
  return min(manhattanDistances)

def part2(wire1Path, wire2Path):
  coordinatesCount1 = calculatePath(wire1Path)
  coordinatesCount2 = calculatePath(wire2Path)
  intersections = [k for k,v in coordinatesCount1.items() if k in coordinatesCount2]
  steps = []
  for intersection in intersections:
    result1 = stepsNeededToReachIntersection(wire1Path, intersection)
    result2 = stepsNeededToReachIntersection(wire2Path, intersection)
    steps.append(result1 + result2)
  return min(steps)


def calculatePath(d):
  directions = d.split(",")
  x, y = 0, 0
  coordinatesCount = defaultdict(int)
  for direction in directions:
    orientation = direction[0]
    stepCount = int(direction[1:])
    k = 0
    if orientation == "U" or orientation == "D":
      k = 1 if orientation == "U" else -1
      for _ in range(stepCount):
        y += k
        coordinatesCount["{}, {}".format(x, y)] += 1
    elif orientation == "L" or orientation == "R":
      k = 1 if orientation == "R" else -1
      for _ in range(stepCount):
        x += k
        coordinatesCount["{}, {}".format(x, y)] += 1
  return coordinatesCount

def stepsNeededToReachIntersection(d, intersection):
  directions = d.split(",")
  x, y = 0, 0
  steps = 0
  for direction in directions:
    orientation = direction[0]
    stepCount = int(direction[1:])
    k = 0
    if orientation == "U" or orientation == "D":
      k = 1 if orientation == "U" else -1
      for _ in range(stepCount):
        y += k
        steps += 1
        key = "{}, {}".format(x, y)
        if key == intersection: return steps
    elif orientation == "L" or orientation == "R":
      k = 1 if orientation == "R" else -1
      for _ in range(stepCount):
        steps += 1
        x += k
        key = "{}, {}".format(x, y)
        if key == intersection: return steps
