def decFunc(data, dicData):
    outputList = []
    for x in data:
        print(x)
        # print(type(x))
        if x.isalpha():
            valueD = dicData.get(x)

            outputList.append(str(valueD))
        else:
            outputList.append(x)
    finalOut = "".join(outputList)

    return finalOut


dictData = {'A': 9}
callFunction = decFunc("A10", dictData)
print(callFunction)
