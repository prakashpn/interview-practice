def finder(num):
    if num in range(100, 500001):
        print(int(num / 2) + 1)
        for i in range(2, int(num / 2) + 1):
            if ((num % i) == 0):
                return False
        else:
            return True

    else:
        return False


print("25-->", finder(25))
print("239-->", finder(239))
print("277-->", finder(277))
print("5000001-->", finder(5000001))
