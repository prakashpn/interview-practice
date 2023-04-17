a = [10, 50, 90]
b = [20, 30, 5]

# result = [5, 10, 20, 30, 50, 90]

result = []
mergeList = a + b
print(mergeList)

for i in range(len(mergeList)):
    for j in range(i + 1, len(mergeList)):
        if mergeList[i] > mergeList[j]:
            mergeList[i], mergeList[j] = mergeList[j], mergeList[i]

print("result: ", mergeList)
