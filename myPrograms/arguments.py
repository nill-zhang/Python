#!/usr/bin/python
# by sfzhang 2016.9.10
from __future__ import print_function

def swap(x, y):
    temp = x
    x = y
    y = temp
    print('x: %s y: %s' % (x, y))


def square_sum(*args):
    print("args: %r" % repr(args))
    print("square_sum: %d" % sum(i**2 for i in args))


def cubic_sum(*args, **kwargs):
    print("args: %r, kwargs: %r" % (repr(args), repr(kwargs)))
    print("cubic_sum: %d" % (sum(j**3 for j in args)+sum(k**3 for k in kwargs.values())))

if __name__ == "__main__":

    input_list = [1, 2]
    input_tuple = (10, 20)
    input_dict = {'x': 11, 'y': 21}
    print('*'*30)
    swap(2, 5)
    print('*' * 30)
    swap(y=34, x='hao')
    print('*' * 30)
    swap(*input_list)
    print('*' * 30)
    swap(*input_tuple)
    print('*' * 30)
    swap(**input_dict)
    print('*' * 30)
    square_sum(1, 3, 4, 5, 6, 7)
    print('*' * 30)
    square_sum(*input_list)
    print('*' * 30)
    square_sum(*input_tuple)
    print('*' * 30)
    square_sum(*input_dict.values())
    print('*' * 30)
    cubic_sum(l=10, m=10, n=10)
    print('*' * 30)
    cubic_sum(*input_list, **input_dict)
    print('*' * 30)


