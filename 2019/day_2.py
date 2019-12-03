inputs = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]

def part1(inputs):
  values = [i for i in inputs]
  for i in range(0, len(values), 4):
    opCode = values[i]
    if opCode == 99:
      return values[0]
    param1 = values[values[i + 1]]
    param2 = values[values[i + 2]]
    param3 = values[i + 3]
    if opCode == 1:
      add(values, param1, param2, param3)
    elif opCode == 2:
      multiply(values, param1, param2, param3)
    else: return values[0]

def add(inputs, param1, param2, param3):
  result = param1 + param2
  inputs[param3] = result

def multiply(inputs, param1, param2, param3):
  result = param1 * param2
  inputs[param3] = result    


def part2(inputs):
  values = [i for i in inputs]
  x = 0
  y = 0
  for i in range(100):
    x = i
    for k in range(100):
      y = k
      values[1] = x
      values[2] = y
      result = part1(values)
      if result == 19690720:
        return 100 * x + y
