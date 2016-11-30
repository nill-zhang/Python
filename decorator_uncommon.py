#!/usr/bin/python
# by sfzhang 2016.11.29
import functools
import time


def clock_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        if args:
            arguments = ', '.join(str(i) for i in args)
        if kwargs:
            keyword_args = ', '.join("%s=%r" % (i, j) for i, j in kwargs.items())
            arguments = arguments + ', ' + keyword_args
        fmt = "{time: %.8f} %s(%s)--->%r"
        print(fmt % (elapsed_time, name, arguments, result))
        return result
    return wrapper

# note that the decorator function must already defined before
# you can use it
@clock_it
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

# functools.lru_cache will store a decorated function's execution results
# next time this function is called with the same arguments
# it can get the results from cache instead of being executed again
# This can save a lot of time for the fibonacci() function, a performance enhancer
@functools.lru_cache()
@clock_it
def fibonacci(num):
    # you can save if-else clauses
    return num if num < 2 else fibonacci(num - 2) + fibonacci(num - 1)


if __name__ == "__main__":

    print("*" * 120)
    factorial(10)
    print("*" * 120)
    fibonacci(10)
    print("*" * 120)