import collections
import itertools

dict1 = {
    "a": 21,
    "b": 5,
    "c": 16
}
dict2 = {
    "a": 9,
    "v": 5,
    "c": 4
}
dict3 = {}
# dict3 = {**dict2, **dict1}
for x in dict1:
    # print(x)
    if x in dict2:
        dict3[x] = dict2[x] + dict1[x]
    else:
        dict3[x] = dict1[x]

for x in dict2:
    if x not in dict1:
        dict3[x] = dict2[x]

print("dict3 :", dict3)

# dict4 = collections.defaultdict(int)
dict4 = {}
for key, value in itertools.chain(dict1.items(), dict2.items()):
    if key in dict4:
        dict4[key] += value
    else:
        dict4[key] = value
print("dict4 :", dict4)
