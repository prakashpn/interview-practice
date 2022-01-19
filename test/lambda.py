# x = list(lambda a=a: a for a in range(1, 6))
x = [lambda a=a: a for a in range(1, 6)]
# print(x)
list1 = []
for x1 in x:
    list1.append(x1())

print(list1)
