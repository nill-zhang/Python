#/usr/bin/python
# by sfzhang 2016.12.22
import random
import time


def paint(sign):

    for i in range(100):
        row = random.randint(0, 100)
        output_string = sign.rjust(row) + " " * (100 - row)
        print(output_string)

    for j in range(100):
        row = random.randint(0, 100)
        output_str = (sign if row == k else " " for k in range(100))
        print(*output_str, sep="")


def snowing_imitation(sign, shift):

    edge = (0, 100)
    for i in range(100):
        row = random.randint(*edge)
        edge = (row-shift, row+shift)
        output_string = sign.rjust(row) + " " * (100 - row)
        print(output_string)
        time.sleep(2)


def heavy_snowing_imitation(sign, density, shift):

    edge = (0, 100)
    line_spots = random.sample(list(range(*edge)), density)
    # print("line_spots: %r" % line_spots)
    for i in range(100):
        output_string = [sign if k in line_spots else " " for k in range(100)]
        # print("output_string: %r" % output_string)
        temp_line_spots = []
        for row in line_spots:
            edge = (row-shift, row+shift)
            row = random.randint(*edge)
            temp_line_spots.append(row)
        line_spots = temp_line_spots[:]
        print(*output_string, sep="")
        # time.sleep(0.1)

if __name__ == "__main__":
    #paint(chr(0x1f495))
    #snowing_imitation(chr(0x273b), 2)
    heavy_snowing_imitation(chr(0x1f495), 100, 3)

