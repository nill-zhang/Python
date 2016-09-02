#!/usr/bin/python
#-*-coding: GBK-*-
#---sfzhang---
'''generate an exe file from python scripts'''
from distutils.core import setup
import cx_Freeze
setup(console=["F:/calysis/calysis.py"])
