def part1(inputs):
  result = 0
  for i in inputs:
    result += calculateNeededFuel(i)
  return result

def part2(inputs):
  result = 0
  for i in inputs:
    result += calculateTotalNeededFuel(i)
  return result

def calculateNeededFuel(payload):
  return payload // 3 - 2

def calculateTotalNeededFuel(payload):
  def recursivelyCalculate(payload, acc):
    neededFuel = calculateNeededFuel(payload)
    if neededFuel > 0:
      acc.append(neededFuel)
      recursivelyCalculate(neededFuel, acc)
      return sum(acc)
  
  return recursivelyCalculate(payload, [])
