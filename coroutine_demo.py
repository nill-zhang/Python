#!/usr/bin/python
# by sfzhang 2016.11.08


def calculate():
    total = 0
    try:
        while True:
            print "before yield"
            n = (yield)
            print "after yield"
            total += n
            print "total is %d" % total
    except GeneratorExit:
        print "stopping calculating..."

if __name__ == "__main__":
    A = calculate()  # nothing was done at this stage
    print "after calling calculate"
    A.next()  # execute until the first yield statement
    print "after calling A.next()"
    for i in xrange(7):
        A.send(i)  # execute yield and loop back until the next yield statement

    A.close()

