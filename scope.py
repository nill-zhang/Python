#!/usr/bin/python
# by sfzhang @2016.11.06

info = "global scope"
number = 3
print info


def first_level():
    info = "first_level info from first_level scope"
    print info
    global info
    info = "global info from first_level scope"
    print info

    def second_level():
        info = "second_level info from second_level scope"
        print info
        global info
        info = "global info from second_level scope"
        print info
        global number
        number = 5
        print "global number is changed to %d" % number

    second_level()


if __name__ == "__main__":
    first_level()
    print info  # global info should be changed after calling first_level()
