#!/usr/bin/env
"""
   bytes() == str() in Python2.7
   The following is experimented in Python3.5
   bytes are immutable
   bytearray is mutable
   they support most of str methods
   from unicode character to byte sequence: encoding
   from byte sequence to unicode character: decoding
   ways to build bytes and bytearray instance:
       A str and an encoding keyword argument.
       An iterable providing items with values from 0 to 255.
       A single integer, to create a binary sequence of that size initialized with null bytes.
       (This signature will be deprecated in Python 3.5 and removed in Python 3.6. See
       PEP 467 — Minor API improvements for binary sequences.)
       An object that implements the buffer protocol (e.g., bytes, bytearray, memory
       view, array.array); this copies the bytes from the source object to the newly created
       binary sequence
"""
>>> a = 'Café'
>>> b = a.encode('utf-8')
>>> b
b'Caf\xc3\xa9'
>>>
>>> b = a.encode('utf-16')
>>> b
b'\xff\xfeC\x00a\x00f\x00\xe9\x00'
>>> len(b)
10
>>> b = a.encode('gb2312')
>>> b
b'Caf\xa8\xa6'
>>> b.decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa8 in position 3: invalid start byte
>>> b.decode('utf-16')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0xa6 in position 4: truncated data
>>> b.decode('gb2312')
'Café'
>>>
>>>
>>> b
b'Caf\xa8\xa6'
>>>
>>> b
b'Caf\xa8\xa6'
>>> b.decode('gbk')
'Café'
>>> b.decode('gb2312')
'Café'
>>>
>>> b.decode('big5')
'Caf谷'
>>>
>>>
>>> c = bytes("abcdef")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string argument without an encoding
>>> c = bytes(b"abcdef")
>>> c
b'abcdef'
>>> c = bytes("abcdef", encoding="utf_8")
>>> c
b'abcdef'
>>> c = bytes("abcdef", encoding="utf_16")
>>> c
b'\xff\xfea\x00b\x00c\x00d\x00e\x00f\x00'
>>>
>>> c.startswith(b"ff")
False
>>> c.startswith(b"\xff")
True
>>> c.startswith("\xff")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: startswith first arg must be bytes or a tuple of bytes, not str
>>> f = bytes.fromhex("3c 4e fe ty")
  File "<stdin>", line 1, in <module>
ValueError: non-hexadecimal number found in fromhex() arg at position 9
>>> f = bytes.fromhex("3c 4e fe ee")
>>> f
b'<N\xfe\xee'
>>> g = bytes([10,20,40,59])
>>> g
b'\n\x14(;'
>>> h = bytes((65,20,140,97])
  File "<stdin>", line 1
    h = bytes((65,20,140,97])
                           ^
SyntaxError: invalid syntax
>>>
>>> h = bytes((65,20,140,97))
>>> h
b'A\x14\x8ca'
>>> h[0]
65
>>> h[1:3]
b'\x14\x8c'
>>> h[0] = b')'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>>
>>> i = bytearray("Café",encoding="utf_16")
>>> i
bytearray(b'\xff\xfeC\x00a\x00f\x00\xe9\x00')
>>> i[0]
255
>>> i[0] = b'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: an integer is required
>>> i[0] = 97
>>> i
bytearray(b'a\xfeC\x00a\x00f\x00\xe9\x00')
>>> i[0:4] = b"a@$%"
>>> i
bytearray(b'a@$%a\x00f\x00\xe9\x00')



>>> import array
>>> numbers = array.array('h', [-2, -1, 0, 1, 2])
>>> octets = bytes(numbers)
>>> octets
# pay attention to the following please
# every element in numbers is a short integer(16 bit)
# from the result we know that
# \xfe\xff == -2
# \xff\xff == -1
# \x00\x00 == 0
# \x01\x00 == 1
# \x02\x00 == 2
# conclusion : least significant bit is on the left
#              because 0001 stands for 1 ffff+0001 is 0
#              so -1 is always represented by ffff in memory
# Creating a bytes or bytearray object from any buffer-like source
# will always copy the bytes.
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'