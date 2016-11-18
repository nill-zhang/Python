#!/usr/bin/env
# by sfzhang 2016.11.12

from collections import namedtuple
from collections import deque
from collections import Counter


def collections_namedtuple():
    field_name = 'name age sex weight'
    person1 = namedtuple('person1', field_name)
    person2 = namedtuple('person2', field_name.split())
    person3 = namedtuple('person3', tuple(field_name.split()))
    a1 = person1('sfzhang', 30, 'Male', 144.00)
    b1 = person1(name='xlyang', weight=110.23, age=24, sex='Female')
    a2 = person2('sfzhang', 30, 144.00, 'Male')
    b2 = person2(name='xlyang', weight=110.23, age=24, sex='Female')
    a3 = person3('sfzhang', 30, 144.00, 'Male')
    b3 = person3(name='xlyang', weight=110.25, age=24, sex='Female')

    for i in (a1, b1, a2, b2, a3, b3):
        print i

    print "person1._fields: ", person1._fields
    c1 = person1._make(['lyzhang', 2, 'Female', 10])
    print "c1: ", c1
    print "c1._asdict()['name']: ", c1._asdict()['name']
    c1._replace(name='xxxxx')  # this one seems doesn't work
    print "c1: ", c1


def collections_deque():
    deque_list = deque((i for i in range(5, 15)), maxlen=10)
    print "deque_list: %s" % deque_list
    deque_list.extend(tuple("sfzhang is a good guy".split()))
    print "deque_list: %s" % deque_list
    deque_list.rotate(2)
    print "rotate 2 steps to the right: %r" % deque_list
    deque_list.rotate(-1)
    print "rotate 1 step to the left: %r" % deque_list
    # append one by one remove the first if reaches maxlen
    deque_list.extend(range(300, 320))
    print "deque_list: %s" % deque_list
    deque_list.extendleft(['a', 'b', 'c', 'd'])
    print "deque_list: %s" % deque_list


def collections_counter():
    counter_dict1 = Counter('sfzhang is a very good guy')
    counter_dict2 = Counter([i for i in range(2, 10)])
    counter_dict3 = Counter(((i, j)for i, j in zip(['xlyang', 'lyzhang'],
                                                   ('mother', 'daughter'))))
    counter_dict4 = Counter((2, 2, 2, 4, 5, 42, 2, 0.23, 8.7, 4, 5, 0))
    print "cdict1: %r" % repr(counter_dict1)
    print "cdict2: %r" % repr(counter_dict2)
    print counter_dict3
    print "cdict4 most common: %r" % repr(counter_dict4.most_common(2))
    counter_dict4.update([1 for i in xrange(10)])
    print "cdict4 most common: %r" % repr(counter_dict4.most_common(2))

if __name__ == "__main__":
    collections_deque()
    print "*"*90
    collections_namedtuple()
    print "*" * 90
    collections_counter()



