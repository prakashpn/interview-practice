list1 = [1, 3, 4, 5]
list2 = [1, 6, 8, 4, 5]
# set1 = set(list1)
# set2 = set(list2)
# if (set1 & set2):
#     print(set1 & set2)

# =========using list comression=============
outpu = [x * 2 for x in list(set(list1).intersection(list2))]
print(outpu)
list3 = []


# lenList1 = len(list1)
# lenList2 = len(list2)

# if (lenList2 > lenList1):
#     for x in range(len(list2)):
#         if (x < len(list1)):
#             mul = list2[x] * list1[x]
#             list3.append(mul)
#         else:
#             list1.append(1)
#             mul = list2[x] * list1[x]
#             list3.append(mul)

# if (lenList2 > lenList1):
#     list3 = [list2[x] * list1[x] for x in range(len(list2)) if x < len(list1)]
# print(list3)


def mulList(list1, list2):
    list3 = [cal(list2, x) * list1[x] for x in range(len(list1))]
    return list3


def cal(list2, x):
    if (x < len(list2)):
        return list2[x]
    else:
        return 1


lenList1 = len(list1)
lenList2 = len(list2)
if (lenList2 > lenList1):
    result = mulList(list2, list1)
    print(result)
else:
    result = mulList(list1, list2)
    print(result)
