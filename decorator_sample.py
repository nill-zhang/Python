#!/usr/bin/python
# by sfzhang 2016.11.09
import functools


class MyDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f()  # Prove that function definition has completed

    def __call__(self):
        print "inside myDecorator.__call__()"

print '\033[1;36m$\033[0m' * 70


@MyDecorator  # equals a_function = MyDecorator(a_function)
def a_function():
    print "inside a_function()"

print "Finished decorating a_function()"

a_function()
print '\033[1;36m$\033[0m' * 70
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
print '\033[1;36m$\033[0m' * 70


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
print '\033[1;36m$\033[0m' * 70


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
print '\033[1;36m$\033[0m' * 70


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
# equals subtraction2 = decorate_subtraction_with_arguments('x - y = %d')(subtraction2)
def subtraction2(x, y):
    print 'inside subtraction2'
    return x-y

subtraction2(1, 99)
print '\033[1;36m$\033[0m' * 70


def bar(func):

    @functools.wraps(func)
    def wrapper():
        """ this is function wrapper's docstring"""
        print("bar")
        return func()
    return wrapper


@bar
def foo():
    """ this is function foo's docstring"""
    print("foo")

print foo.__name__
print foo.__doc__

print '\033[1;36m$\033[0m' * 70


def class_method_decorator(func):
    counter = [0]  # you also can use a global variable outside this function

    # if don't use *args and **kwargs, you should use (self,name) as the parameters here
    def wrapper_function(*args, **kwargs):
        counter[0] += 1
        print "this is the %d time," % counter[0] + func(*args, **kwargs)
    return wrapper_function


class People(object):

    def __init__(self, origin):
        self.origin = origin

    @class_method_decorator
    def get_age(self, name):
        return 'My name is %s and am from %s' % (name, self.origin)

sf = People('Asia')
sf.get_age('Shaofeng Zhang')
sf.get_age('Alex')
sf.get_age('Helen')
sf.get_age('George Martin')
print '\033[1;36m$\033[0m' * 70


