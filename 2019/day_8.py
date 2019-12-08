def splitImageIntoLayers(imageData, w, h):
    layers = []
    for i in range(0, len(imageData), w * h):
        layer = []
        for k in range(h):
            layer.append(imageData[i + w * k : (i + w) + w * k])
        layers.append(layer)
    return layers


def countNumberInLayer(number, layer):
    return layer.count(number)


def part1(imageData, w, h):
    layers = splitImageIntoLayers(imageData, w, h)

    minZeroCount = countNumberInLayer("0", layers[0])
    targetLayer = layers[0]

    for layer in layers:
        zeroCount = countNumberInLayer("0", layer)
        if zeroCount < minZeroCount:
            minZeroCount = zeroCount
            targetLayer = layer

    oneCount = countNumberInLayer("1", targetLayer)
    twoCount = countNumberInLayer("2", targetLayer)

    return oneCount * twoCount


def part2(imageData, w, h):
    layers = splitImageIntoLayers(imageData, w, h)
    joinedLayers = ["".join(i) for i in layers]

    pixelIndex = 0
    result = ""

    while pixelIndex < w * h:
        finalPixel = joinedLayers[0][pixelIndex]
        for layer in joinedLayers:

            currentPixel = layer[pixelIndex]

            if finalPixel == "2" and currentPixel != "2":
                finalPixel = currentPixel
                break
        pixelIndex += 1
        result += finalPixel

    codes = {"0": "  ", "1": "##", "2": " "}

    finalLayers = splitImageIntoLayers(result, w, h)[0]

    for layer in finalLayers:
        layer = [codes[i] for i in layer]
        print("".join(layer))
