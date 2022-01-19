# def cal(num):
#     if (num > 5):
#         print("num is greatre than 5")
#         # return "num is greatre than 5"
#     elif (num == 5):
#         print("num is equal 5")
#     else:
#         print("num is less than 5")
#
#
# call_m = cal(10)
# print(call_m)

def fib(num):
    if num < 0:
        print("cant not proceed")
    elif num == 1 or num == 2:
        return 1
    elif num == 0:
        return 0
    else:
        return fib(num - 1) + fib(num - 2)


fib_result = fib(9)
print(fib_result)
