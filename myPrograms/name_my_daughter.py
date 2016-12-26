#!usr/bin/python
# by sfzhang 2016.12.11
import itertools


def generate_name():
    unicode_code_points = [(0x4e00,  0xA000),
                           (0x3400,  0x4dc0),
                           (0x20000, 0x2a6e0),
                           (0x2a700, 0x2b820),
                           (0xf900,  0xfb00),
                           (0x2f800, 0x2fa20),
                           (0x9fa6,  0x9fcc)]

    # combined = (range(i, j) for i, j in unicode_code_points)
    # a better way to build a iterable of iterables
    combined_code_points = itertools.starmap(range, unicode_code_points)
    flattened_code_points = itertools.chain(*combined_code_points)
    for n in flattened_code_points:
        # one for display, one for output
        twins = itertools.tee(map(chr, (0x5f20, n)), 2)
        print(''.join(twins[0]))
        try:
            if input("you like the name?"):
                yield twins[1]
        except EOFError:
            print("*" * 120)
            raise StopIteration


def print_name():
    a = ("".join(i) for i in generate_name())
    print("*"+" ".join(a).center(113)+"*")
    print("*" * 120)
    # for i in generate_name():
    #     print("".join(i))


if __name__ == "__main__":
    print_name()

