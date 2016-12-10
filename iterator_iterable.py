#!/usr/bin/python
import re
from reprlib import repr


class Sentence1(object):
    word_pattern = re.compile(r"\w+")

    def __init__(self, text):
        self.text = text
        self.words = re.findall(Sentence.word_pattern, self.text)

    # if you implement __iter__ or __getitem
    # the instance will be iterable , whatever
    # you put inside those two will be returned as an iterator
    # to iterate over
    def __getitem__(self, item):
        return self.words[item]

    def __repr__(self):
        return "Sentence(%s)" % repr(self.text)


def test_sentence1(text):
    a = Sentence(text)
    print("%r" % a)
    print(a[3])
    print("self" in a)
    # instead of using for i in a: print a
    # you can use the following, what a smart
    # solution, unpack iterable into positional arguments
    print(*a, sep="\n")

    # return an iterator when you call iter on a iterable
    b = iter(a)
    # iterator has __next__ attribute
    print("*" * 120)
    print(next(b))
    print(next(b))
    print("*" * 120)
    print(*b, sep="\n")
    print("*" * 120)
    # The following will generate nothing, because b is an
    # iterator and was already iterated over once
    # StopIteration is handled for iterable unpacking
    # list comp, generator exp, for loop
    print(*b, sep="\n")
    print("*" * 120)


if __name__ == "__main__":
    test_sentence1("sfzhang is a good guy, he do everything him self wow12s, 23erw23")
