import inspect
import pprint

def func(name:str, age: int, *posi, salary:'int>0'=3000, **kword ) -> str:
   """ func gives some info about itself"""
   pprint.pprint("locals:\n" + locals())
   pprint.pprint("globals:\n" + globals())
   pprint('positional arguments:' + ' '.join(posi))
   for i in kword.items():
       pprint('{}-->{}'.format(*i)
    def newfunc():
       nonlocal age
       age += 1
       return age
   return newfunc()


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
