def getNextNumber(number):
  nextNumber = number + 1
  while len(str(nextNumber)) == 6:
    if "".join(sorted(str(nextNumber))) == str(nextNumber): return nextNumber
    nextNumber += 1

def hasPair(number):
  string = str(number)
  for i in range(len(string)-1):
    pair = string[i:i+2]
    if pair[0] == pair[1]: return True
  return False

def part1(number1, number2):
  count = 0
  while number1 < number2:
    if hasPair(number1):
        count += 1
    number1 = getNextNumber(number1)

  return count


# Part2 TBC
