def whatFloor(inputText):
	goUp = inputText.count('(')
	goDown = inputText.count(')')
	return goUp - goDown