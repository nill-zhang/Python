#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang  2012.9.10---
import os
import re
import os.path
import xml.dom.minidom
import sys
t1 = os.popen('type E:\\2.txt')
t2 = os.popen('type E:\\ak.py')
t3 = os.popen('type E:\\delDir.py')
print(t1.read())
print(t2.read())
print(t3.read())