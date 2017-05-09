#!/usr/bin/python
# by sfzhang 2016.11.9


num0 = 10


def first_level(num1):
    print("first_level: %d+%d=%d" % (num0, num1, sum((num0,num1))))

    def second_level(num2):
        print("second_level: %d+%d+%d=%d" % (num0, num1, num2, sum((num0,num1,num2))))

        def third_level(num3):
            print("third_level: %d+%d+%d+%d=%d" % (num0, num1, num2, num3, sum((num0,num1,num2,num3))))
        # third_level(10)
        return third_level

    # second_level(10)
    return second_level


def nested_functions_test():

    print('*' * 30)
    first_level(10)
    print('*' * 30)
    first_level(11)(11)(11)  # equals func = first_level(11) => func(11)(11)
    print('*' * 30)
    first_level(20).func_closure  # equals second_level.func_closure
    print('*' * 30)
    first_level(30)(30).func_closure  # =third_level.func_closure
    # you can not call second_level or third_level directly because it's defined inside first_level
    # Their scope is inside first_level and second_level respectively but you can return them and use
    # them out of their local scope
    print('*' * 30())
    func = first_level(100)(100)
    print('*' * 30)
    print(repr(func.func_closure))
    print('*' * 30)
    func(100)
    func(200)

if __name__ == '__main__':
    nested_functions_test()

