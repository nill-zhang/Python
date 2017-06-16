import inspect
import pprint

def func(name:str, age: int, *posi, **kword, salary:'int>0'=3000) -> str:
   """ func gives some info about itself"""
   pprint.pprint("locals:\n" + locals())
   pprint.pprint("globals:\n" + globals())
   pprint('positional arguments:' + ' '.join(posi))
   pprint('{}-->{}'.format(*kword.items()))


def func_caller_variants():
    """call func in different ways"""

def func_inspector():
    print("annotations: ", func.__annotations__)
    print("closure: ", func.__closure__)

    print("annotations: ", func.__annotations__)

    print("annotations: ", func.__annotations__)

    print("annotations: ", func.__annotations__)


    func.__code__.
    a = inspect.signature(func)
    for param in a.parameters.values():
        print('{:10s}{:30s}{:50s}'.format(param.name, str(param.kind), str(param.default)))
