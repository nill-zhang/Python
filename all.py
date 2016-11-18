#!/usr/bin/python
# -*- coding: GBK -*-
# 2012.2.1 by  sfzhang


def bnfAnalysisXml():
    impl = getDOMImplementation()
    doc = impl.createDocument(None, "root", None)
    root = doc.documentElement
    batrec = doc.createElement("batrec")
    root.appendChild(batrec)
    f = open('D:/work/python/batreclog-' + str(time.time()) + '.xml', 'a+')  # time.time() 生成当前时间戳
    f.write('<?xml version="1.0" encoding="GB2312"?>' + '\n')
    f.write('<?xml-stylesheet type="text/xsl" href="./ISR-CORRECTRECO-REPORT-XSLFILE.xsl"?>' + '\n\n')
    root.setAttribute('calog_dir', 'bnflog.txt')
    f.write(root.toprettyxml())
    tt = open('bnflog.txt', 'r')
    lines = tt.readlines()
    tt.close()
    print(lines)
    f.close()


def count(a):
    return len(a)


def operate_on_key():
    source_list = ['sfzhang', 'xlyang', 'qshu', 'jchu', 'xlz']
    # count must return, otherwise it won't work
    print "sorted: %r" % sorted(source_list, key=count)
    print "max: %s" % max(source_list, key=count)
    print "min: %s" % min(source_list, key=count)

if __name__ == "__main__":

    operate_on_key()



