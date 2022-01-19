a = [1, 2, 3, 2, 2, 1, 3, 4, 2, 4, 4, 2, 42, 5, 6, 36, 7, 8, 9, 8, 7, 8, 9]
outList = {}
for x in a:
    # outList[x] = a.count(x)
    if x in outList:
        outList[x] += 1
    else:
        outList[x] = 1

print(outList)

d1 = {'key1': 50, 'key2': 100, 'key3': 200}
d2 = {'key1': 200, 'key2': 100, 'key4': 300}
for key in d2.keys():
    if key in d1.keys():
        d1[key] = d1.get(key) + d2.get(key)
    else:
        d1[key] = d1.get(key)

print(d1)
