#!/usr/bin/env
# by sfzhang 2016.12.15
"""
The whole idea of this module is to detect user keypress
if any stdin keypress happens, do that, other wise keep doing
this, haven't got a solution yet.
"""
import sys
import termios
import tty
import time
import select
import threading
import random


def test_select():
    while True:
        input("like this name? ")
        a, _, _ = select.select([sys.stdin], [], [], 2)
        # time.sleep(2)
        if a:
            input("more detail? ")
            b, _, _ = select.select([sys.stdin], [], [], 2)
            if b:
                print("张")
            print("saved")


def test_tty():
    fd = sys.stdin.fileno()
    original_setting = termios.tcgetattr(fd)
    tty.setraw(sys.stdin)
    if sys.stdin.read(1):
        print("got something")
    else:
        print("get nothing")

    # for i in range(10):
    #    print("ASD", end="\r\n")
    termios.tcsetattr(fd, termios.TCSADRAIN, original_setting)


def input_with_timeout(prompt, timeout):
    while True:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            print("got something")
            break
            # if sys.stdin.readline().rstrip('\n'):
        else:
            print("\tnothing")


def input_with_timeout2():
    # print(prompt, end="\t")
    print_name()
    while True:
        timer = threading.Timer(3, input_with_timeout2)
        usr_str = None
        try:
            timer.start()
            # a = sys.stdin.read(1)
            # if a:
            #    print("something")
            usr_str = input("how is it")
        except KeyboardInterrupt:
            print("print all names")
        timer.cancel()
        if usr_str in ("y", "yes"):
            print("usr_str: %r" % usr_str, "Showing details")
            time.sleep(5)


def print_name():
    name = ["alex", "sfzhang", "xlyang", "jchu", "qshu"]
    print(random.choice(name), "like the name ?\n  ")


def merge():
    fd = sys.stdin.fileno()
    original_setting = termios.tcgetattr(fd)
    while True:
        print_name()
        tty.setraw(fd)
        timer = threading.Timer(4, print_name)
        timer.start()
        usr_input = sys.stdin.read(1)
        if usr_input in ('y', 'yes'):
            print("details", end="\n")
            timer.cancel()

    termios.tcsetattr(fd, termios.TCSADRAIN, original_setting)


if __name__ == "__main__":
    merge()

