#!/usr/bin/python
# -*- coding: GBK -*-
#2012.4.13 by  sfzhang
import os
#t =open('S:/POI_CALLOG/POI0510.scp','r')
#empty = open('S:/POI_CALLOG/empty.txt','w')
#notEmpty = open('S:/POI_CALLOG/notEmpty.txt')
t =open('E:/POI0510.scp','r')
empty = open('E:/empty.txt','w')
notEmpty = open('E:/notEmpty.txt','w')
for eachline in t.readlines():
    s = eachline.strip()
    if s != '':
        if os.path.isfile(s):
            size = os.path.getsize(s)
            if size ==0:
                empty.write(s+'\n')
            else:
                notEmpty.write(s+'\n')
t.close()
empty.close()
notEmpty.close()
