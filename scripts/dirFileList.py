#!/usr/bin/python
# -*- coding: GBK -*-
#2012.5.2 by  sfzhang
import os
list = os.listdir('E:/测试环境/abnf')
t = open('E:/测试环境/result.txt', 'w')
for eachline in list:
    t.write('QISRWaveformSearch ,'+'"'+'D:/abnf/'+eachline+'"'+',,'+'\n')
t.close()
