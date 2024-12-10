def flatten_list(lst):
    result = []
    for element in lst:
        print(isinstance(element, list))
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