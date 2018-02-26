# Solution for Part 1

def whatFloor1(inputText):
	goUp = inputText.count('(')
	goDown = inputText.count(')')
	return goUp - goDown

# Solution for Part 2

def causedTogoIntoBasement(inputText):
	floor = 0
	for i in inputText:
		if i == '(':
			floor += 1
		else:
			floor -= 1

		if floor == -1:
			return i + 1