a = [3, 7, 10, 85, 16]
b = [23, 14, 45, 67, 77]
c = []
length = len(a)
print(length)
for x in range(length):
    # print(x)
    if (a[x] < b[x]):
        c.append(a[x] * b[x])
    else:
        c.append(a[x] / b[x])

print(c)
print("\n")


A = "Instagram has made photography more accessible to a wider audience."
outList = {}
for x in A.lower():
    # outList[x] = a.count(x)
    if x in outList:
        outList[x] += 1
    else:
        outList[x] = 1
print(outList)
