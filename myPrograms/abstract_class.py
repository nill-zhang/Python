#!/usr/bin/env
# by sfzhang 2016.12.04
import abc
import random


# for python3 plus and before version 3.4
# class Bingo(metaclass=abc.ABCMeta)


class Bingo(abc.ABC):
    """ An Abstract Base Class """
    # for python2.7
    # __metaclass__ = abc.ABCMeta
    # Note that we didn't implement __init__
    # in our ABC

    @abc.abstractmethod
    def pick(self):
        """ randomly remove and return an element
            must raise LookupError if the instance
            is empty
        """

    @abc.abstractmethod
    def load(self, iterable):
        """load new elements from an iterable"""

    # subclasses don't need to implement concrete methods
    # they can implement smarter concrete methods
    # concrete methods must only use abstract methods, concrete
    # methods and class attributes
    def loaded(self):
        """ return true if there is at least one item, false otherwise"""
        return bool(self.inspect())

    def inspect(self):
        """ return a tuple with sorted items"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        # this step is necessary because you've emptied the instance
        # you have to put those elements back
        self.load(items)
        return tuple(sorted(items))


class Fake_SubClass(Bingo):
    """ this is a subclass that only implements
        one of its two must-have abstractmethods
        when you initial an instance, the type error will be
        raised
    """
    def pick(self):
        return "pick"


class BingoCage(Bingo):

    def __init__(self, items):
        self._random = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._random.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except ValueError:
            raise LookupError(" no items left in %r" % self)

    # you can implement other methods in subclasses of ABC
    def __call__(self):
        self.pick()


class LotteryBlower(Bingo):

    def __init__(self, iterable):
        self.random = random.SystemRandom()
        self.items = list(iterable)

    def load(self, iterable):
        self.items.extend(iterable)

    def pick(self):
        try:
            # you need to catch IndexError if you use the commented alternate
            # item_index = self.random.randint(0,len(self.items))
            # self.items.pop(item_index)
            item = self.random.choice(self.items)
            self.items.remove(item)
        except ValueError:
            raise LookupError("no items left in  %r" % self)
        return item

    def loaded(self):
        return bool(self.items)

    def inspect(self):
        return tuple(sorted(self.items))


# register this class to abc Bingo
@Bingo.register
class BingoVirtual(list):
    """A virtual subclass"""
    def pick(self):
        if self:
            position = random.SystemRandom().randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("no items in %r" % self)

    # a class attribute set to list.extend
    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


def test_bingo():
    try:
        flawed_instance = Fake_SubClass()
    except TypeError:
        print("can not instantiate a new instance of Fake_SubClass")

    print(Bingo.__subclasses__())
    # BingoVirtual does not inherit any attributes and methods from Bingo,
    # so you can not find it in Bingo.__subclasses__(),
    print(list(Bingo._abc_registry))

    a_list = BingoVirtual((i for i in range(10)))
    print(a_list.pick())
    print(a_list)
    print(isinstance(a_list, Bingo))
    print(issubclass(BingoVirtual, Bingo))
    # because BingoVirtual doesn't inherit anything from Bingo
    # method resolution order will not try to look methods in
    # Bingo
    print(BingoVirtual.__mro__)


def test_subclasshook():
    import collections

    class A(object):
        """ A class satisfying subclasshook of collections.Sized"""
        def __len__(self):
            return 2

    class B(object):
        """ A class satisfying subclasshook of collections.Iterator"""
        def __iter__(self):
            return 222

        def __next__(self):
            return 22222
    a = A()
    b = B()
    # in our scenario, we didn't inherit, nor did we
    # register our defined class to abc
    # we just implement some abstract methods that
    # can be checked in those abc's __subclasshook__
    # then we also subclass our classes to abcs
    print(issubclass(A, collections.Sized))
    print(isinstance(a, collections.Sized))
    print(issubclass(B, collections.Iterator))
    print(isinstance(b, collections.Iterator))

if __name__ == "__main__":
    test_bingo()
    test_subclasshook()


