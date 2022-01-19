def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

    return function_wrapper


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


# cll_foo = foo
# cll_foo("Hi")

# # cll_foo = our_decorator(foo)
# cll_foo("Hi")
foo("Hi Decorator")
