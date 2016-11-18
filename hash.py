#!/usr/bin/python
# by sfzhang 2016.11.16
import pprint


def count_occurrence(fdir):
    """ this function counts word occurrence from a file"""
    occur = {}
    with open(fdir) as f:
        # enumerate takes one parameter(a iterable) usually
        # it has an optional parameter which defines the start index
        for line_no, line in enumerate(f, 1):
            for column_no, word in enumerate(line.strip().split(), 1):
                # it is very import here, that we use setdefault
                # if the key does not exist, we assign a empty list
                # and return a reference to the value: a new list object
                # they later we append every occurrence to the reference
                # which will update the object as well, because they are
                # the same thing and point to the same memory address
                occur_location = occur.setdefault(word, [])
                occur_location.append((line_no, column_no))
        f.close()

    for m, n in occur.items():
        print m, n


def construct_dict():
    """ways to construct a dict"""
    dict_a = dict(([i, j] for i in range(1, 6) for j in 'abcde'))
    dict_b = dict([[i, j] for i in range(10, 16) for j in 'abcde'])
    dict_c = dict(((i, j) for i in range(20, 26) for j in 'abcde'))
    dict_d = dict([(i, j) for i in range(30, 36) for j in 'abcde'])
    dict_e = dict(a=1, b=2, c=3, d=4, e=5)
    # dict comprehension,note that enumerate is similar
    # to generator, it is one-time iterable
    dict_f = {i: j.upper() for i, j in enumerate('sfzhangisagoodguy') if i > 10}
    dict_g = dict(zip(('sfzhang', 'xlyang'), [30, 29]))

    for dt in [dict_a, dict_b, dict_c, dict_d, dict_e, dict_f, dict_g]:
        pprint.pprint(dt)


def is_hashable(param):
    for obj in param:
        try:
            hash(obj)
        except:
            print "%s is not hashable and can not be used as a dict key" % repr(obj)
        else:
            print "%s is hashable" % repr(obj)


if __name__ == "__main__":
    construct_dict()
    count_occurrence("zen.txt")
    test_list = ['sfzhang', 4, 5.5, (2, 'hello', 4.5),
                 (2, 'hello', (3, 6)), (2, 'hello', [4.5]),
                 [2, 3, 'good'], ['what', 32.9, (2, 0.5)]]
    is_hashable(test_list)

