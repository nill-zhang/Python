#!/usr/bin/python
# by sfzhang 2016.11.30
"""
   if an object is a container, its shallow copy will duplicate another
   container, but the inner container elements(lists,tuples) share the same
   references with the original container's inner container elements,
   if you change inner mutable elements(lists)the duplicate container will
   be changed accordingly, if you change immutable elements(tuples), you
   assign the inner elements to reference a new immutable elements which
   differs from the respective inner elements within the duplicate container.
   Thus, in this situation,the duplicate container will not change

"""


import copy


class Limo(object):

    def __init__(self, passenger=None):
        if passenger is None:
            self.passenger = []
        else:
            self.passenger = list(passenger)

    def pick_up(self, name):
        self.passenger.append(name)
        print("Inside pick_up, Owner: %r" % self)

    def drop_off(self, name):
        self.passenger.remove(name)


def test_instance():
    instance_a = Limo(["Smith", "Sam", "Sarah"])
    instance_b = copy.copy(instance_a)
    instance_c = copy.deepcopy(instance_a)
    print("id(a): %r\tid(b): %r\tid(c): %r" % (id(instance_a), id(instance_b), id(instance_c)))
    instance_a.pick_up("John")
    print("instance_a.passenger: %r" % instance_a.passenger)
    print("instance_b.passenger: %r" % instance_b.passenger)
    print("instance_c.passenger: %r" % instance_c.passenger)
    print("id(a.passenger): %r" % id(instance_a.passenger), end='\t')
    print("id(b.passenger): %r" % id(instance_b.passenger), end='\t')
    print("id(c.passenger): %r" % id(instance_c.passenger))

    # class methods has different id from instance methods
    # deep copys of instances share the same references of instance methods
    print("id(a.pick_up): %r" % id(instance_a.pick_up), end='\t')
    print("id(b.pick_up): %r" % id(instance_b.pick_up), end='\t')
    print("id(c.pick_up): %r" % id(instance_c.pick_up))
    instance_c.pick_up("Cindy")
    print("instance_a.passenger: %r" % instance_a.passenger)
    print("instance_b.passenger: %r" % instance_b.passenger)
    print("instance_c.passenger: %r" % instance_c.passenger)
    print("id(a.drop_off): %r" % id(instance_a.drop_off), end='\t')
    print("id(b.drop_off): %r" % id(instance_b.drop_off), end='\t')
    print("id(c.drop_off): %r" % id(instance_c.drop_off))
    print("id(Limo.pick_up): %r\t id(Limo.drop_off): %r" % (id(Limo.pick_up), id(Limo.drop_off)))


def test_list():
    list_a = [32, [2, 3, 4], ("Peter", "Alex", "Kim")]
    list_b = list_a
    list_c = list_a[:]  # or you can use list_c = list(a), both are shallow-copy statements
    print("id(list_a): %r\tid(list_b): %r\tid(list_c): %r"
          % (id(list_a), id(list_b), id(list_c)))
    print("id(list_a[1]): %r\tid(list_b[1]): %r\tid(list_c[1]): %r"
          % (id(list_a[1]), id(list_b[1]), id(list_c[1])))
    print("id(list_a[2]): %r\tid(list_b[2]): %r\tid(list_c[2]): %r"
          % (id(list_a[2]), id(list_b[2]), id(list_c[2])))
    list_a[1].append(5)
    # the following two statements have no effects on list_c
    # because they are operations on singletons, not container elements
    list_a.append("xxxxx")
    list_a.remove(32)
    # because the third element is a tuple, which is immutable
    # so the following equals getting the value of the tuple plus it with
    # ("Ivy", "Williams") and assign the third element to the new tuple object
    list_b[1] += ("Ivy", "Williams")
    print("After change inner list and tuple".ljust(100, "*"))
    print("id(list_a[1]): %r\tid(list_b[1]): %r\tid(list_c[1]): %r"
          % (id(list_a[1]), id(list_b[1]), id(list_c[1])))
    print("id(list_a[2]): %r\tid(list_b[2]): %r\tid(list_c[2]): %r"
          % (id(list_a[2]), id(list_b[2]), id(list_c[2])))
    print("list_a: %r" % list_a)
    print("list_b: %r" % list_b)
    print("list_c: %r" % list_c)
    list_c[2] += ("Ann", "Lee")
    print("list_a: %r" % list_a)
    print("list_b: %r" % list_b)
    print("list_c: %r" % list_c)
    print("*" * 100)
if __name__ == "__main__":
    test_list()
    test_instance()



