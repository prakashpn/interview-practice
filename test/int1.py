strngo = "Hi all, My name is Tom...i am originaly from India!"
# spclC=".,!"

splitString0 = strngo.split()
print(splitString0)
sumSt = sum(len(x) for x in splitString0)
print(sumSt)
avgS = sumSt / len(splitString0)

print("avgS --> ", avgS)
# print("avgS --> ", avgS.)

removeS = "".join(strt for strt in strngo if strt.isalnum())
print(removeS)

