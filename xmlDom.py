#!/usr/bin/python
#-*-coding: GBK-*-
import  xml.dom.minidom
import time
xml1 = xml.dom.minidom.parse('D:/work/xml/note.xml')
t = open('D:/work/xml/a.xml','w')
nodes = xml1.getElementsByTagName('note')
for everyNode in nodes:
    print('nodeType:'+repr(everyNode.childNodes[1].firstChild.nodeType))
    print('nodeName:'+everyNode.childNodes[1].firstChild.nodeName)
    print('nodeValue:'+repr(everyNode.childNodes[1].firstChild.nodeValue))
    print('attributes:'+repr(everyNode.childNodes[1].firstChild.attributes))
xml1.writexml(t)
time.sleep(10) 