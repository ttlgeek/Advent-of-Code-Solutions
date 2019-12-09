from collections import defaultdict


def part1(boxIds):
    appearsTwice = 0
    appearsThrice = 0
    for boxId in boxIds:
        lettersCount = defaultdict(int)
        hasLetterAppearsTwice = False
        hasLetterAppearsThrice = False
        for i in boxId:
            lettersCount[i] += 1
        for k, v in lettersCount.items():
            if v == 2:
                hasLetterAppearsTwice = True
            elif v == 3:
                hasLetterAppearsThrice = True

            if hasLetterAppearsTwice and hasLetterAppearsThrice:
                break
        if hasLetterAppearsTwice:
            appearsTwice += 1
        if hasLetterAppearsThrice:
            appearsThrice += 1
    return appearsTwice * appearsThrice


def part2(boxIds):
    for i in range(len(boxIds)):
        boxId = boxIds[i]

        for k in range(len(boxIds)):
            compareTo = boxIds[k]

            if compareTo == boxId:
                continue
            differentLetters = 0
            for i in range(len(compareTo)):
                if boxId[i] != compareTo[i]:
                    differentLetters += 1
            if differentLetters == 1:
                return "".join(
                    [boxId[i] for i in range(len(boxId)) if boxId[i] == compareTo[i]]
                )
