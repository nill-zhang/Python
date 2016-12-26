#!/usr/bin/python
# by sfzhang 2016.11.29

registry = []


def register(func):
    """a decorator putting func referencesinto a list"""
    # note1:
    # a wrapper function definition inside a decorator
    # is not necessary, as long as the decorator return a function
    # object, so try imaging all the stuff you can do with argument function object
    # inside a decorator, before you return a function object
    #
    # note2:
    # decorators are run when the modules where they were defined
    # are imported
    print("running inside register decorating %r" % func)
    registry.append(func)
    return func


@register
def func1():
    print("inside func1")


@register
def func2():
    print("inside func2")


def func3():
    print("inside func3")


if __name__ == "__main__":
    print("inside main")
    print(registry)
    func1()
    func2()
    func3()

# Running results from a console
# C:\Users\Admin\Documents\GitHub\Python_General>python decorator_abnormal.py
# running inside register decorating <function func1 at 0x0000022CE9BDC730>
# running inside register decorating <function func2 at 0x0000022CE9BDC7B8>
# inside main
# [<function func1 at 0x0000022CE9BDC730>, <function func2 at 0x0000022CE9BDC7B8>]
# inside func1
# inside func2
# inside func3
