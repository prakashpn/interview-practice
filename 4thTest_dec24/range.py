# make a range function using generator
def my_range(start, stop=None, step=1):
    if stop is None:  # If only one argument is provided
        start, stop = 0, start
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


# Example usage
for i in my_range(1, 10, 2):
    print(i)
