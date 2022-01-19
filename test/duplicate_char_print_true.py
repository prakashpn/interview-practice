def getName(name):
    dict1 = {}
    for char in name:
        # print(char)
        counts = name.count(char)
        while counts > 1:
            dict1[char] = counts
            break

    print(dict1)
    # print(not dict1)
    if not dict1:
        return False
    else:
        return True


print(getName("catt"))
print(getName("cat"))
