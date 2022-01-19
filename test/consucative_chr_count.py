a = "wwwwaaadexxxxxxaarrrrr"
c = ""
d = []

dict1 = {}
count = 0
for x in range(0, len(a)):
    if x == 0:
        count = 1
    if x >= 1:
        if a[x] == a[x - 1]:
            count += 1
            c = a[x] + str(count)
            # print("c data: ", c)

        else:
            d.append(c)
            count = 1
            c = a[x] + str(count)
            # print("c data: ", c)

    if x == len(a) - 1:
        d.append(c)

# print(d)
output = "".join(d)
print(output)
