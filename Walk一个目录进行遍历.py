#!/usr/bin/python
#-*-coding = UTF-8-*-
import os

t = open('D:/python/python/oswalk.txt','w')
for root, dirs, files in os.walk('D:\\work'):
    t.write('-'*40+'\n')
    t.write('root:'+repr(root)+'\n')
    t.write('dir names:'+repr(dirs)+'\n')
    t.write('files:'+repr(files)+'\n')
    print(repr(root))
    print(repr(dirs))
    print(repr(files))
t.close()
