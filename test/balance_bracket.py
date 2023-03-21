# Input: "((a+b)*c)/g)+(d-e*((f))"
# Valid: (a+b)
# Invalid: )a+b(

Input = "((a+b)*c)/g)+(d-e*((f))"
# Input = "({}[][{(a+b)-b}])"

for x in Input:
    # print(x)
    vald = []
    if x == "(" or x == "{" or x == "[":
        for y in Input:
            vald.append(y)

# def checkBalance(str1):
#     count = 0
#     ans = False
#     for i in str1:
#         if i == "(" or i == "{" or i == "[":
#             count += 1
#         elif i == ")" or i == "}" or i == "]":
#             count -= 1
#         if count < 0:
#             return ans
#     if count == 0:
#         return not ans
#     return ans


# str1 = input("Enter a string of brackets: ")
# print("Given string is balanced :", checkBalance(Input))

# count = 0
# a = False
# valid = []
# for x in Input:
#     print(x)
#     if (x == "("):
#         count += 1
#         print("Count ( :", count)
#     elif (x == ")"):
#         count -= 1
#         print("Count ):", count)
#     # if (count < 0):
#     #     print(a)
#     # if (count == 0):
#     #     print(not a)
