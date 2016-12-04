#!/usr/bin/env
# by sfzhang 2016.12.04
import abc


# for python3 before 3.4
# class Bingo(metaclass=abc.ABCMeta)
class Bingo(abc.ABC):
    # for python2.7
    # __metaclass__ = abc.ABCMeta
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
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Bingo):
    pass


class LotteryBlower(Bingo):
    pass


class BingoVirtual(object):
    pass

if __name__ == "__main__":
    pass