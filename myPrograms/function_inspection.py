import inspect
from pprint import pprint
import operator


class a(object):
    pass


def b():
    pass


def outer_func(p1, p2, p3, *args, keyword=33, **kword):
    print("outer_func locals:")
    pprint(locals())
    print("outer_func globals:")
    pprint(globals())
    pprint('outer positional arguments:' + ' '.join(str(parg) for parg in args))
    print("outer keyword arguments:")
    for item in kword.items():
        print('{}-->{}\n'.format(*item))

    def inner_func(p4, p5):
        nonlocal p1, p2
        print("inner_func locals:")
        pprint(locals())
        print("inner_func globals:")
        pprint(globals())
        pprint('inner positional arguments:' + ' '.join(str(parg) for parg in args))
        print("inner keyword arguments:")
        for each in kword.items():
            print('{}-->{}\n'.format(*each))
    return inner_func


def func(name: str, ranking: int, *posi, salary: 'int>0'=3000, **kword ) -> str:
    """ an high-order function"""
    def wrapped_func(incr):
        """a wrapped function which can change nonlocal variables"""
        # ranking and salary are free variables
        # wrapped_func can use
        # func.__code__.co_cellvars == wrapped_func.__code__.co_freevars
        nonlocal ranking, salary
        ranking -= 1
        salary += incr
        return ranking, salary
    return wrapped_func


def func_call_variants():
    """call func in different ways"""
    func("sfzhang", 3, 2, 3, 4, 5, salary=8999, noexist=333)
    # func(2, 3, 34, 54, 5, name="alex", salary=222, ranking=31) func() will get multiple values for argument 'name'
    # func("helen", salary=222,33) positional arguments should be ahead of keyword argument
    func("nova", 9, 1, 2, 3, 4, 5, 6, noexist=3, salary=22222)


def attrs_inspector(*items, attr_list):
    """ compare attributes of different elements in items"""
    get_attrs = operator.attrgetter(*attr_list)
    attr_groups = zip(attr_list, *map(get_attrs, items))
    for group in attr_groups:
        print("{:16s}\t{:95s}\t{:95s}".format(*[str(item) for item in group]))


def attrs_comparison():

    func_attrs = ["__annotations__", "__closure__",
                    "__defaults__", "__dict__",
                    "__doc__", "__kwdefaults__",
                    "__qualname__", "__name__"]

    func_code_attrs = list(set(dir(b.__code__)) - set(dir(a())))
    print(" " * 16+'\t'+'\t'.join((func.__name__.ljust(95),
                                   func("Ann", 2, 2000).__name__.ljust(95)))+"\n")
    # you must specify keyword argument attr_list
    # because otherwise it can not differentiate which is positional argument and
    # which is keyword argument
    attrs_inspector(func, func("sfzhang", 3), attr_list=func_attrs)
    attrs_inspector(func.__code__, func("sfzhang", 3).__code__, attr_list=func_code_attrs)


def inspector_using_inspect():
    sig = inspect.signature(func)
    sig_wrapped = inspect.signature(func("Jim", 2))
    for s in (sig, sig_wrapped):
        for param in s.parameters.values():
            print('{:10s}{:30s}{:50s}'.format(param.name, str(param.kind), str(param.default)))


def getinfo():
    wrapped = outer_func(1, 2, 3, 4, 5, 6, 7, 8, kw1="kw1")
    wrapped(-1, -2)

if __name__ == "__main__":
    for f in [getinfo, inspector_using_inspect, attrs_comparison, func_call_variants]:
        print("*" * 200)
        f()
