#!/usr/bin/env
# by sfzhang 2016.12.1
import math


class Vector(object):
    """ a user-defined class behaves like ducks, support duck-typing"""

    def __init__(self, horizontal, vertical):
        self.horizontal = float(horizontal)
        self.vertical = float(vertical)

    def __iter__(self):
        return (item for item in (self.horizontal, self.vertical))

    def __repr__(self):
        # you can also use type(self).__name__
        return "%s(%r,%r)" % (self.__class__.__name__, self.horizontal, self.vertical)

        # maximum recursion depth exceeded, we can not use repr, because repr will call the
        # instance's __repr__, which will cause infinite recursion

        # return repr(self.__class__(self.horizontal, self.vertical))
        # string object(xxx.__name__) is not callable, in addition to the repr call
        # return repr(self.__class__.__name__(self.horizontal, self.vertical))

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return (self.horizontal == other.horizontal) and \
               (self.vertical == other.vertical)

    def __abs__(self):
        return math.sqrt(self.horizontal ** 2 + self.vertical ** 2)

    def __add__(self, other):
        # you can also use type(self)
        return self.__class__(self.horizontal + other.horizontal, self.vertical + other.vertical)

    def __bool__(self):
        return bool(abs(self))


def decorated_print(func):
    def wrapper(*args, **kwargs):
        new_args = (s.ljust(30) for s in args)
        func(*new_args, **kwargs)
    return wrapper


@decorated_print
def my_print(*args, **kwargs):
    print(*args, **kwargs)


def test_vector():
    triangle_a = Vector(3, 4)
    my_print("repr(triangle_a):", "%r" % triangle_a)
    my_print("triangle_a:", "%s" % triangle_a)
    my_print("triangle_a.horizontal:", "%r" % triangle_a.horizontal)
    my_print("triangle_a.vertical:", "%r" % triangle_a.vertical)
    triangle_b = Vector(6, 8)
    my_print("abs(triangle_b):", "%r" % abs(triangle_b))
    triangle_c = triangle_a + triangle_b
    my_print("triangle_c:", "%s" % triangle_c)
    triangle_d = eval(repr(triangle_c))
    my_print("triangle_d:", "%r" % triangle_d)
    my_print("abs(triangle_d):", "%r" % abs(triangle_d))
    print(type(triangle_d)(9, 15))

if __name__ == "__main__":
    test_vector()



