# make a range function using generator
# def range_f():
#     yield 1
#     yield 2
#     yield 3
#
#
# a = range_f()
# for x in a:
#     print("Value :", x)

# lst = [[1, 2], [3, 4], [[4], [6]]]
# # output = [1,2,3,4,4,6]
#
# output = []
# for x in lst:
#     for y in x:
#         output.append(y)



def flatten_list(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            # Recursive call for sublist
            result.extend(flatten_list(element))
        else:
            # Add non-list elements to the result
            result.append(element)
    return result

# Input list
lst = [[1, 2], [3, 4], [[4], [6]]]

# Flatten the list
output = flatten_list(lst)
print(output)