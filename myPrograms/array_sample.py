#!/usr/bin/python
# by sfzhang 2016.11.17

import array
import random
import numpy
import time


def standard_array():
    float_array = array.array('f', (random.random() for i in range(5)))
    int_array = array.array('i', (random.randint(-1, 50) for j in range(5)))
    string_array = array.array('c', 'sfzhang xlyang lyzhang')
    print("float array item size: %d" % float_array.itemsize)
    print("int array item size: %d" % int_array.itemsize)
    print("string array item size: %d" % string_array.itemsize)
    float_array.append(1111.1111)
    print("float array : %r" % float_array)
    float_file = open("float_array.bin", 'wb')
    float_array.tofile(float_file)
    float_file.close()
    float_file = open("float_array.bin", 'rb')
    float_array2 = array.array('f')
    float_array2.fromfile(float_file, len(float_array))
    float_file.close()
    print("float array2 : %r" % float_array2)
    float_array.extend(random.random() for k in range(5))
    print("float array after extension %r" % float_array)
    float_file = open("float_array.bin", 'rb')
    first_number = float_file.read(4)
    float_file.close()
    print("first number: %s" % first_number)


def numpy_array():
    numpy_int_array = numpy.arange(40)
    print("shape %r" % numpy_int_array.shape)
    numpy_int_array.shape = 5, 8
    print(numpy_int_array)
    print(numpy_int_array[2]) # get third row
    print(numpy_int_array[:, 2])  # get third column
    print(numpy_int_array[2, 4])  # get third row fifth column

    print(numpy_int_array.transpose())

    numpy_float_array2 = numpy.arange(0, 1, 0.00000002, dtype=float)
    print("len: %d" % len(numpy_float_array2))
    start = time.clock()
    numpy_float_array2 *= 10  # times every element by 10
    finish = time.clock()
    print("takes %s to perform operations a 50000000 element array" % str(finish-start))
    print(numpy_float_array2[-3:])
    numpy.save("float_numpy", numpy_float_array2)
    numpy_float_array3 = numpy.load("float_numpy.npy")
    print(numpy_float_array3[-3:])


if __name__ == "__main__":
    standard_array()
    numpy_array()

