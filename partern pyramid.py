"""
* # # # #
* * # # #
* * * # #
* * * * #
* * * * *
"""


def pypart(n):
    i = 1
    while (i <= n):
        # print(" " * (n - i) + "*" * i)
        print("* " * i + "# " * (n - i))
        i += 1


# Driver Code
n = 3
pypart(n)
