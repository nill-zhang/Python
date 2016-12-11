#!/usr/bin/python
# by sfzhang @2016.12.10
from contextlib import contextmanager
import sys


class Mirror(object):
    """a context manager class implements enter and exit special methods"""

    def __init__(self, hand_writing):
        self.original_write = sys.stdout.write
        self.hand_writing = hand_writing

    def __enter__(self):
        sys.stdout.write = self.reverse_write
        return self.hand_writing

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is NameError:
            print("can not find variable")
            return True


@contextmanager
def mirror(hand_writing):
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield hand_writing
    except NameError:
        print("can not find variable")
    finally:
        sys.stdout.write = original_write


def test_class_mirror():
    pass


def test_func_mirror():
    pass

if __name__ == "__main__":
    pass

