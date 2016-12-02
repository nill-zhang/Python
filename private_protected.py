#!/usr/bin/env
# by sfzhang 2016.12.1


class Coordinate(object):
    """ an object is hashable only if its immutable, but this example shows
        that you can implement customized __hash__ special methods
    """
    def __init__(self, x, y):
        self.__horizontal = float(x)
        self.__vertical = float(y)

    # set public read-only property self.horizontal
    @property
    def horizontal(self):
        return self.__horizontal

    # set public read-only property self.vertical
    @property
    def vertical(self):
        return self.__vertical

    def __hash__(self):
        return hash(self.horizontal) ^ hash(self.vertical)


class CoordinateSlots(object):
    """a class defining __slots__ class attribute"""
    # if a class defines __slots__, all the created instance will
    # share __slots__ instead of have a per-instance __dict__
    # it defines the immutable attributes instances of this class should
    # have, if you want to keep inherited attributes you also should
    # define those in __slots__, otherwise, it ignores them
    __slots__ = ("__horizontal", "__vertical")

    def __init__(self, x, y):
        self.__horizontal = x
        self.__vertical = y


class SubCoordinate(Coordinate):
    def __init__(self, x, y):
        # call parent class, initiate attributes with x, y
        # note that the instantiated instance will get
        # four attributes, two private from parent classes, another
        # two from current class with distinct names
        super().__init__(x, y)
        self.__horizontal = x
        self.__vertical = y


def test_hash():
    point = Coordinate(3.9, 4.6)

    print("hash(point): %r" % hash(point))
    print("H: %r" % point.horizontal)
    print("V: %r" % point.vertical)
    try:
        point.horizontal = 5
    except Exception as e:
        print(*e.args)
    dict1 = dict()
    dict1[point] = [point.horizontal, point.vertical]
    print(dict1)
    point._Coordinate__horizontal = 7.7
    point._Coordinate__vertical = 8.8
    print("hash(point): %r" % hash(point))
    print("H: %r" % point.horizontal)
    print("V: %r" % point.vertical)
    dict1[point] = [point.horizontal, point.vertical]
    print(dict1)
    point2 = Coordinate(9, 14.6)
    print(set([point, point2]))


def test_private_attributes():
    # print attribute of instance point
    obj_coordinate = Coordinate(1, 1)
    print("[Coordinate] object.__dict__ %r" % obj_coordinate.__dict__)

    obj_sub_coordinate = SubCoordinate(1.1, 1.1)
    print("[SubCoordinate] object.__dict__ %r" % obj_sub_coordinate.__dict__)


def test_slots():
    obj_coordinate = Coordinate(2, 2)
    print("[Coordinate] object.__dict__:  %r" % obj_coordinate.__dict__)
    # assign a new attribute to instance obj_coordinate, should be ok
    obj_coordinate.new_attribute = "xxxxx"
    print("[Coordinate] object new attribute added:  %r" % obj_coordinate.new_attribute)

    obj_coordinate_slots = CoordinateSlots(2.2, 2.2)
    try:
        print("[CoordinateSlots] object.__dict__:  %r" % obj_coordinate_slots.__dict__)
    except Exception as e:
        print(*e.args)
    finally:
        print("[CoordinateSlots] object.__slots__:  %s" % repr(obj_coordinate_slots.__slots__))
    try:
        # assign new attribute to instance, which should fail because of class attribute
        # __slots__ already defined the attributes instances should have, which can not
        # be changed
        obj_coordinate_slots.new_attribute = "xxxx"
    except Exception as e:
        print(*e.args)


if __name__ == "__main__":
    test_private_attributes()
    print("*" * 100)
    test_slots()

