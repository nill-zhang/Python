#!/usr/bin/env
# sfzhang  2016.11.22


def flatten(lst):
    global flattened_lst
    head, *tail = lst  # python3 support
    if isinstance(head, list) | isinstance(head, tuple):
        flatten(head)
    else:
        flattened_lst.append(head)
    if tail:
        flatten(tail)


if __name__ == "__main__":
    flattened_lst = []
    container = [[1, 3], ("sfzhang", "xlyang", "lyzhang"), [[['whoa'], 7.888]], [[[(90,)]]], 3.444, 'Hey']
    flatten(container)
    print(flattened_lst)