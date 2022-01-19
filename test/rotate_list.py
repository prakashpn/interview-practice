list1 = [2, 56, 1, 6, 7]


# reversO = [x for x in reversed(list1)]
# print(reversO)

# rotate array
def rotate(list, num):
    outList = []

    for x in range(len(list) - num, len(list)):
        outList.append(list[x])

    for y in range(0, len(list) - num):
        outList.append(list[y])

    return outList


print(rotate(list1, 2))
