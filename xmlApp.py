#!/usr/bin/python
#-*-coding: GBK-*-
import xml.dom.minidom
xmlImple = xml.dom.minidom.getDOMImplementation()
dom = xmlImple.createDocument(None, 'catalog', None)
fileXml = open('F:/Recognize.xml','w')
fileXml.write('<?xml version="1.0" encoding="GB2312"?>'+'\n')
fileXml.write('<?xml-stylesheet type="text/xsl" href="../xsl_def/ISR-RECO-REPORT-XSLFILE.xsl"?>'+'\n')
root = dom.documentElement
root.setAttribute('calog_dir',"D:\\4.1\\aitalk_calog\\log3-28\\13-54-2")
item = dom.createElement('item')
text = dom.createTextNode('test')
item.appendChild(text)
root.appendChild(item)
fileXml.write(root.toprettyxml())



