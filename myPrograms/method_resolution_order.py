#!/usr/bin/python
# by sfzhang 2016.12.9
import tkinter


class A(object):
    def ping(self):
        print("Class A[ping]:", self)


class B(A):
    def pong(self):
        print("Class B[pong]:", self)


class C(A):
    def pong(self):
        print("Class C[pong]", self)


class D(B, C):
    def ping(self):
        print("Class D[ping]:", self)

    def pingpong(self):
        print("Class D[pingpong]: ", self)
        self.ping()
        self.pong()
        super().ping()  # delegate method call to superclass
        super().pong()  # according to mro, this will call class B's pong method
        C.pong(self)  # explicitly delegate method call to superclass C by bypassing mro


class E(C, B):
    """ Another Class with a different inheritance order to Class D"""
    def ping(self):
        print("Class E[ping]:", self)

    def pingpong(self):
        print("Class E[pingpong]: ", self)
        self.ping()
        self.pong()
        super().ping()
        super().pong()
        C.pong(self)


def print(_mro(cls):

    try:
        clses = (obj.__name__ for obj in cls.__mro__)
        print("method resolution order of %r:" % cls)
        print(', '. join(clses))
    except AttributeError:
        print("can not print method resolution order of %r" % cls)

if __name__ == "__main__":
    d = D()
    d.ping()
    print(_mro(D))
    print(_mro(E))
    e = E()
    d.pingpong()
    e.pingpong()
    print(D.__dict__)
    print(_mro)(tkinter.Text)
    print(_mro)("fefef")
    print(dir(d))
    print(dir(B))

