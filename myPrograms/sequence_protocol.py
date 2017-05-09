#!/usr/bin/env
# by sfzhang 2016.12.3
import collections
import array
import reprlib

Cards = collections.namedtuple("Cards", "suit rank")
suits = [str(i) for i in range(2, 11)] + list("JQKA")
ranks = "Diamonds Spades Hearts Clubs".split()


class CardGame(object):
    def __init__(self):
        self._cards = [Cards(suit, rank) for suit in suits for rank in ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


class MultiDimensionalVector(object):

    type_code = "f"

    def __init__(self, dimensions):
        self._components = array.array(self.type_code, dimensions)

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        compo_str = reprlib.repr(self._components)
        list_str = compo_str[compo_str.find("["): compo_str.rfind("]") + 1]
        return "%s(%s)" % (type(self).__name__, list_str)

    def __getitem__(self, index):

        # check the index type to make sure
        # we support slicing
        # you can compare the difference between this method and
        # the previous class's __getitem__ method
        print(("index type: %r" % type(index)))
        if isinstance(index, slice):
            return type(self)(self._components[index])
        else:
            return type(self)([self._components[index]])


if __name__ == "__main__":
    my_cards = CardGame()
    my_cards[2]
    print(("*" * 120))
    a = MultiDimensionalVector((2, 3, 4, 5, 7.7, 9.2, 0.45, 777, 23.43, 0.123, 2.0123, 4.2309))
    # note that we'd better not call a protected attribute(start by single underscore)
    # outside a class, here, we just want to display its content, to check the
    # returned value of a sliced instance is still a instance
    print(a, type(a), a._components, sep="\n")

    print(("*" * 120))
    b = a[2:9]
    print(b, type(b), b._components, sep="\n")

    print("*" * 120)
    b = a[5]
    print(b, type(b), b._components, sep="\n")
