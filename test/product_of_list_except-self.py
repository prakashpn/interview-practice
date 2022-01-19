# def productExceptSelf(inputList):
#     outlist = []
#     for x in range(len(inputList)):
#         list2 = inputList[:]
#         list2.pop(x)
#         muti = 1
#         for x in range(len(list2)):
#             muti *= list2[x]
#         outlist.append(muti)
#     return outlist
#
#
# list = [1, 2, 3, 4]
# print(list)
# final = productExceptSelf(list)
# print(final)
import numpy as np
from sqlalchemy.util import reduce
from operator import mul


# def productExceptSelf(inputList):
#     # a = np.array(inputList)
#     # out = a.prod() / a
#     # print("out ", out)
#     a = reduce(mul, inputList)
#     out = [a / x for x in inputList]
#     return out

def productExceptSelf(arr):
    n = len(arr)
    # Base case
    if (n == 1):
        print(0)
        return

    # Allocate memory for temporary arrays left[] and right[]
    left = [0] * n
    right = [0] * n

    # Allocate memory for the product array
    prod = [0] * n

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[n - 1] = 1

    # Construct the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    # Construct the right array
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Construct the product array using
    # left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]
    prod1 = []
    # print the constructed prod array
    for i in range(n):
        # print(prod[i], end=' ')
        prod1.append(prod[i])
    print(prod1)
    return prod1


list = [1, 2, 3, 4]
print(list)
final = productExceptSelf(list)
# print(final)
