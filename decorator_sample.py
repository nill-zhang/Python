#!/usr/bin/python
# by sfzhang 2016.11.09


class MyDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f()  # Prove that function definition has completed

    def __call__(self):
        print "inside myDecorator.__call__()"

print '\033[1;36m$\033[0m' * 39


@MyDecorator  # equals a_function = MyDecorator(a_function)
def a_function():
    print "inside a_function()"

print "Finished decorating a_function()"

a_function()
print '\033[1;36m$\033[0m' * 39
# running results:
# inside myDecorator.__init__()
# inside a_function()
# Finished decorating a_function()
# inside myDecorator.__call__()


def decorate_addition(function):
    number = 'x + y = %d'

    def stop(*args, **kwargs):
        print 'inside decorate_addition'
        print number % function(*args, **kwargs)
    return stop


@decorate_addition
def addition(x, y):
    print 'inside addition'
    return x+y

addition(2, 7)
print '\033[1;36m$\033[0m' * 39


class SubtractionDecorator(object):

    def __init__(self, func):
        print "inside SubtractionDecorator.__init__"
        self.func = func
        self.number = 'x - y = %d'

    def __call__(self, *args, **kwargs):
        print "inside SubtractionDecorator.__call__"
        print self.number % self.func(*args, **kwargs)


@SubtractionDecorator
def subtraction(x, y):
    print 'inside subtraction'
    return x-y

subtraction(8, 3)
print '\033[1;36m$\033[0m' * 39


class SubtractionDecorator1(object):

    def __init__(self, info):
        print "inside SubtractionDecorator1.__init__"
        self.info = info

    def __call__(self, f):
        print "inside SubtractionDecorator1.__call__"

        def new_func(*args, **kwargs):
            print self.info % f(*args, **kwargs)
        return new_func


@SubtractionDecorator1('x - y = %d')
def subtraction1(x, y):
    print 'inside subtraction1'
    return x-y

subtraction1(1, 10)
print '\033[1;36m$\033[0m' * 39


def decorate_subtraction_with_arguments(info):
    print 'inside decorate_subtraction_with_arguments info: %s' % info

    def decorate_subtraction(func):
        print 'inside decorate_subtraction'

        def new_func(*args, **kwargs):
            print 'inside new_func'
            print info % func(*args, **kwargs)
        return new_func
    return decorate_subtraction


@decorate_subtraction_with_arguments('x - y = %d')
def subtraction2(x, y):
    print 'inside subtraction2'
    return x-y

subtraction2(1, 99)
print '\033[1;36m$\033[0m' * 39
