#!/usr/bin/python
# -*- coding: GBK -*-
#2012.5.2 by  sfzhang
import os
list = os.listdir('E:/���Ի���/abnf')
t = open('E:/���Ի���/result.txt', 'w')
for eachline in list:
    t.write('QISRWaveformSearch ,'+'"'+'D:/abnf/'+eachline+'"'+',,'+'\n')
t.close()
