def reverse_by_swap(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length-1-i] = lst[length-1-i], lst[i]


def reverse_by_recursion(lst):
    print(lst)
    if len(lst) == 1:
        return lst
    else:

        # why I can not use append????
        # because when the recursion finish the base case
        # it will append the second but last element to the
        # base case list, the return value is None, then the recursion
        # will call the append on the third but last element with
        # None

        # return (reverse_by_recursion(lst[1:])).append(lst[0])
        return reverse_by_recursion(lst[1:]) + [lst[0]]


def reverse_test():
    a = [1, 2, 3, 4, 5, 6, 7]
    reverse_by_swap(a)
    assert a == [7, 6, 5, 4, 3, 2, 1], "reverse_by_swap fails"
    b = reverse_by_recursion(a)
    assert b == [1, 2, 3, 4, 5, 6, 7], "reverse_by_recursion fails"


if __name__ == "__main__":
    reverse_test()
