#!/usr/bin/python
# -*- coding: GBK -*-
#2011.1.15 by  sfzhang
import xml.dom.minidom
import time
def bnfAnalysisXml():
	impl = xml.dom.minidom.getDOMImplementation()
	doc = impl.createDocument(None, "root", None)
	root = doc.documentElement
	batrec = doc.createElement("batrec")
	root.appendChild(batrec)
	f = open('D:/work/python/batreclog-'+str(time.time())+'.xml', 'a+')  # time.time() 生成当前时间戳
	f.write('<?xml version="1.0" encoding="GB2312"?>' + '\n')
	f.write('<?xml-stylesheet type="text/xsl" href="./ISR-CORRECTRECO-REPORT-XSLFILE.xsl"?>' + '\n')
	root.setAttribute('calog_dir','bnflog.txt')
	f.write(root.toprettyxml())
	f.close()
bnfAnalysisXml()


