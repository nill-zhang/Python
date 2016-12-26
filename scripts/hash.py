#!/usr/bin/python
# by sfzhang 2016.11.16
import pprint
import collections
import types


def count_occurrence_normal(fdir):
    """ this function counts word occurrences from a file"""
    occur = {}
    with open(fdir) as f:
        # enumerate takes one parameter(a iterable) usually
        # it has an optional parameter which defines the start index
        for line_no, line in enumerate(f, 1):
            for column_no, word in enumerate(line.strip().split(), 1):
                # it is very import here, that we use setdefault
                # if the key does not exist, we assign a empty list
                # and return a reference to the value: a new list object
                # they later we append every occurrence to the reference
                # which will update the object as well, because they are
                # the same thing and point to the same memory address
                occur_location = occur.setdefault(word, [])
                occur_location.append((line_no, column_no))
                # this is a better way :)
                # occur.setdefault(word, []).append((line_no,column_no))
        f.close()

    for m, n in occur.items():
        print m, n


def count_occurrence_defaultdict(fdir):
    """ this function is another way to implement the previous one"""
    # this is a dict use default_factory(list)when the key is missing
    # and return the list object'reference as the missing key's value
    occur = collections.defaultdict(list)
    with open(fdir) as f:
        # enumerate takes one parameter(a iterable) usually
        # it has an optional parameter which defines the start index
        for line_no, line in enumerate(f, 1):
            for column_no, word in enumerate(line.strip().split(), 1):
                # if key(word) is missing, create a empty list before append
                # behind the scene: the __getitem__is invoked, and when it
                # can not look up the key, it will call the default_factory
                # to add a key and value pair
                occur[word].append((line_no, column_no))
        f.close()

    for m, n in occur.items():
        print m, n


class dict_with_strkey(dict):
    """ this is a user-defined dict class using string keys
        if a key lookup fails, the key will be converted to
        its string type and then do the lookup
    """
    def __missing__(self, key):
        # when a dict invoke __missing__ method, it
        # already fails the key lookup
        # lets check whether is a string, if it is
        # no need to lookup further, raise keyError
        # indicates no such key exists
        # the if statement also provides a exit point
        # for the following return statement
        if isinstance(key, str):
            raise KeyError("%s does not exist in our dictionary" % key)
        # this step will probably invoke the __missing__ methods again
        # when the str(key) is not found
        return self[str(key)]

    def get(self, key, default=None):
        # 1. do normal key lookup
        # 2. do __missing__
        # 3. if __missing__, raised an KeyError
        #    return default no matter it's given or not
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        # don't use key in self, it will create recursive
        # invocation of __contains__
        return key in self.keys() or str(key) in self.keys()

def construct_dict():
    """ways to construct a dict"""
    dict_a = dict(([i, j] for i in range(1, 6) for j in 'abcde'))
    dict_b = dict([[i, j] for i in range(10, 16) for j in 'abcde'])
    dict_c = dict(((i, j) for i in range(20, 26) for j in 'abcde'))
    dict_d = dict([(i, j) for i in range(30, 36) for j in 'abcde'])
    dict_e = dict(a=1, b=2, c=3, d=4, e=5)
    # dict comprehension,note that enumerate is similar
    # to generator, it is one-time iterable
    dict_f = {i: j.upper() for i, j in enumerate('sfzhangisagoodguy') if i > 10}
    dict_g = dict(zip(('sfzhang', 'xlyang'), [30, 29]))

    for dt in [dict_a, dict_b, dict_c, dict_d, dict_e, dict_f, dict_g]:
        pprint.pprint(dt)

'''
# types.MappingProxyType is provided since Python3.3
# it is a wrapper class of dict type, it provides read-only dynamic
# view of the original dict, changes can not made through it.

def dict_proxy():
    original_dict = dict(name='sfzhang', age=29, weight=140.00, original_dict='Asia')
    proxy_dict = types.MappingProxyType
    try:
        proxy_dict['name'] = 'xlyang'
    except TypeError:
        print "assignment failed"
    original_dict.__setitem__('DOB', '1985-10-13')
    print proxy_dict['DOB']
'''


def is_hashable(param):
    for obj in param:
        try:
            hash(obj)
        except TypeError:
            print "%s is not hashable and can not be used as a dict key" % repr(obj)
        else:
            print "%s is hashable" % repr(obj)


if __name__ == "__main__":
    construct_dict()
    count_occurrence_normal("zen.txt")
    test_list = ['sfzhang', 4, 5.5, (2, 'hello', 4.5),
                 (2, 'hello', (3, 6)), (2, 'hello', [4.5]),
                 [2, 3, 'good'], ['what', 32.9, (2, 0.5)]]
    is_hashable(test_list)
    test_dict = dict_with_strkey((['2015', 'last year'],
                                  ['2014', 'year before last year'],
                                  ['2016', 'current year'],
                                  ['2017', 'next year']))

    print "test dict_with_strkey.__missing__"
    print test_dict[2014]
    print test_dict['2014']
    try:
        print test_dict[2011]
    except KeyError:
        print "2011 is not a valid key"

    print "test dict_with_strkey.get"
    print test_dict.get(2015)
    print test_dict.get(2011)
    print test_dict.get(2011, 'long long time ago')

    print "test dict_with_strkey.__contains__"
    print '2012' in test_dict
    print 2012 in test_dict
    print '2011' in test_dict




