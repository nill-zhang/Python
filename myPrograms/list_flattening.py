#!/usr/bin/env
# sfzhang  2016.11.22
import collections


def list_flatten(lst):
    global flattened_lst
    head, *tail = lst  # python3 support
    if isinstance(head, list) | isinstance(head, tuple):
        list_flatten(head)
    else:
        flattened_lst.append(head)
    if tail:
        list_flatten(tail)


def iterable_flatten1(iterable):
    """ this func take an iterable of iterables and flatten it"""
    for item in iterable:
        if isinstance(item, collections.Iterable) and not isinstance(item, str):
            # yield from itself instead of calling itself
            yield from iterable_flatten1(item)
        else:
            yield item


def iterable_flatten2(iterable):
    for item in iterable:

        if isinstance(item, collections.Iterable) and not isinstance(item, str):
            iterable_flatten2(item)
        else:
            print(item, end=" ")


def test_iterable_flatten():
    a = [(2, 3, 3), 3.5, [2, 3, 4, 3.7, (233, 2, 0.32, (232, 0.11))], 0]
    b = [j for j in iterable_flatten1(a)]
    print(*b)
    iterable_flatten2(a)
    print("\n")
    # the following  two line of code will cause RecursionError
    # if you don't add the second condition because, even every single
    # character string is also considered an iterable
    # after we add the second condition, we will single strings out, print them
    container = [[1, 3], ("sfzhang", "xlyang", "lyzhang"), [[['whoa'], 7.888]], [[[(90,)]]], 3.444, 'Hey']
    iterable_flatten2(container)

if __name__ == "__main__":
    # flattened_lst = []
    # container = [[1, 3], ("sfzhang", "xlyang", "lyzhang"), [[['whoa'], 7.888]], [[[(90,)]]], 3.444, 'Hey']
    # list_flatten(container)
    # print(flattened_lst)
    test_iterable_flatten()
