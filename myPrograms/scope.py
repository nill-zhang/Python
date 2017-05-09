#!/usr/bin/python
# by sfzhang @2016.11.06
from pprint import pprint

info = "global scope"
number = 3
print(info)


def first_level():
    info = "first_level info from first_level scope"
    print(info)
    global info
    info = "global info from first_level scope"
    print(info)

    def second_level():
        info = "second_level info from second_level scope"
        print(info)
        global info
        info = "global info from second_level scope"
        print(info)
        global number
        number = 5
        print("global number is changed to %d" % number)

    second_level()

x = 7
y = 0


def fun1():
    y = 11
    z = x + 1
    print("fun1: x is %d, y is %d" % (x, y))
    pprint(fun1.__globals__)
    print(repr(fun1.__closure__))

    def fun2():
        y = 22
        z = 77
        print("fun2: x is %d, y is %d" % (x, y))
        pprint(fun2.__globals__)
        print(repr(fun2.__closure__))

        def fun3():
            y = 33
            print("fun3: x is %d, y is %d, z is %d" % (x, y, z))
            pprint(fun3.__globals__)
            print(repr(fun3.__closure__))
        fun3()
    fun2()


if __name__ == "__main__":
    first_level()
    print(info)  # global info should be changed after calling first_level()
    fun1()
