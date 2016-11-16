#!/usr/bin/env

from collections import namedtuple
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

