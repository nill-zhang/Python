#!/usr/bin/env
# sfzhang 2016.11.18


def set_construct():
    set_a = set(['sfzhang', 'xlyang', 'xlyang', 'xlyang', 'john', 'alex', 'bob'])
    set_b = set(i for i in set_a)
    set_c = set([1, 23, 2, 3, 4, 2, 3, 2])
    set_c.update((2, 23, 42, 2, 5, 22222, 0.23))
    print('\n'.join((repr(i) for i in (set_a, set_b, set_c))))
    try:
        set_c.add([2, 4])
    except TypeError:
        print("Set element must be hashable,[2,4] is not!")
    # return a set unifies all the sets
    set_d = {chr(i) for i in range(30, 40)}  # set comprehension
    return set_a | set_b | set_c | set_d


def set_operations(myset):

    print(myset)
    print("intersection: %r" % repr(myset & set([i for i in xrange(3)])))
    print("Union: %r" % repr(myset | set(['hey,there'])))
    print("Difference: %r" % repr(myset - myset))
    print("Symmetric Difference: %r" % repr(myset ^ set([i for i in xrange(5, 15)])))


if __name__ == "__main__":

    set_operations(set_construct())