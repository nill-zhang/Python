#!/usr/bin/python
# by sfzhang 2016.11.7


class CountDown(object):
    """a custom class which supports iteration"""

    def __init__(self, start):
        print "\033[1;36m instantiating instance \033[0m"
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration("no more values to iterate")
        else:
            r = self.start
            self.start -= 1
            return r

    def __del__(self):
        print "\033[1;35m destroying instance \033[0m"


def countdown(number):
    print "before while"
    while number > 0:
        print "inside while and before yield"
        yield number
        print "inside while and after yield"
        number -= 1


if __name__ == "__main__":
    # A = CountDown(10)
    B = countdown(5)
    print "before for loop"
    # for i in A:
    #     print i
    for j in B:
        print "j is %s" % j
