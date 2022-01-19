from itertools import cycle, islice

listS = [1, 2, 3, 4, 5, 6]
grp = 4
itr = 7
i = 0
newList = cycle(listS)
print(newList)

for x in range(itr):
    print(list(islice(newList, 0, grp)))
