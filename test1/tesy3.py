import collections

a = [2, 3, 4, 5, 5]
b = [3, 2, 4, 5]
if a == b:
    print("eql")
else:
    print("Not")
frequency = collections.Counter(a)
print(dict(frequency))

dict1 = {"a": 2, "b": 3, "c": 4}
dict2 = {"b": 3, "a": 2, "c": 4}
if dict1 == dict2:
    print("eql")
else:
    print("Not")
