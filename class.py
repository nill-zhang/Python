#！/usr/bin/python
# by sfzhang 2016.11.26
"""
   defaultdict has a default_factory argument which you can use
   to generate a (key, value) item if any key is missing
   this argument can be anything that is callable and the return value
   from this callable is used as the new default value for that key

"""
from collections import defaultdict


def missing_element():
    global missing_count
    missing_count += 1
    return "missing"


class CountMissing(object):
    """ """
    def __init__(self):
        self.missing_count = 0

    def missing_element(self):
        self.missing_count += 1
        return "missing"


class BetterCountMissing(object):
    """ """
    def __init__(self):
        self.missing_count = 0

    def __call__(self):
        self.missing_count += 1
        return "missing"


if __name__ == "__main__":
    missing_count = 0
    keyword_list = ["name", "age", "weight", "Date of Birth", "address"]
    personal_info = (("company", "IFLYTEK"),
                     ("name", "shaofeng zhang"),
                     ("height", "174"),
                     ("spouse", "helen"),
                     ("address", "409 20 Humberline Drive"))

    # normal user-defined function as default_factory for defaultdict
    mydict1 = defaultdict(missing_element, personal_info)

    # class method as default_factory for defaultdict
    instance1 = CountMissing()
    mydict2 = defaultdict(instance1.missing_element, personal_info)
    # class special method __call__ as stateful default_factory for defaultdict
    instance2 = BetterCountMissing()
    mydict3 = defaultdict(instance2, personal_info)

    for i in keyword_list:
        print(mydict1[i], mydict2[i], mydict3[i], sep="\t")
    print(missing_count, instance1.missing_count, instance2.missing_count, sep="\t")
    print(mydict1, mydict2, mydict3, sep="\n")

