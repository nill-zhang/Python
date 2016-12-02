#!/usr/bin/python
# by sfzhang 2016.11.08


def calculate():
    total = 0
    try:
        while True:
            print("before yield")
            n = (yield)
            print("after yield")
            total += n
            print("total is %d" % total)
    except GeneratorExit:
        print("stopping calculating...")


def decorate_grep(func):
    print("before start,func is %r" % func)

    def start(*args, **kwargs):
        print("args: %r , kwargs: %r" % (args, kwargs))
        cor = func(*args, **kwargs)

        # for python2.7, you can use cor.next() directly
        cor.__next__()
        return cor
    print("after start, func is %r" % func)
    return start


@decorate_grep
def grep(pattern):
    print("find pattern %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


if __name__ == "__main__":
    A = calculate()  # nothing was done at this stage
    print("after calling calculate")
    A.__next__()  # execute until the first yield statement
    print("after calling A.next()")
    for i in range(7):
        A.send(i)  # execute yield and loop back until the next yield statement

    A.close()
    B = grep("python")
    B.send("I like python, which is an excellent language")
    B.send("what did you say??")
    B.send("I said python is fantastic, I can not live without it")
