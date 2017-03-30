#!/usr/bin/env
# sfzhang 2016/07/02
from __future__ import print_function
import re
import os
import sys
import shutil
import collections
import pprint
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(message)s")


def copy_onetype_files(src, des, regex):
    if not os.path.exists(os.path.abspath(src)):
        logging.debug(src, "does not exist !")
        sys.exit()
    if not os.path.exists(des):
        os.makedirs(des)
    result_list = []
    for item in os.walk(os.path.abspath(src)):
        for eachfile in item[2]:
            if re.compile(r'(\.'+regex+')$', re.I)\
                                .search(eachfile):
                logging.debug(os.path.join(item[0], "\033[92m{}\033[0m".\
                       format(eachfile)))
                shutil.copy(os.path.join(item[0], eachfile), des)
                result_list.append(os.path.join(des, eachfile))
    return result_list
                

def del_onetype_files(src, regex, parent=None):
    if parent:
        for eachfile in os.walk(os.path.abspath(src)).next()[2]:
            if re.compile(r'(\.'+regex+')$',re.I)\
                                 .search(eachfile):
                logging.debug(os.path.join(os.walk(os.path.abspath(src)).next()[0],
                              "\033[92m{}\033[0m".format(eachfile)))
                os.remove(os.path.join(os.walk(os.path.abspath(src)).next()[0],eachfile))
        sys.exit()            
    for item in os.walk(os.path.abspath(src)):
        for eachfile in item[2]:
            if re.compile(r'(\.'+regex+')$', re.I)\
           .search(eachfile):
                logging.debug(os.path.join(item[0], "\033[92m{}\033[0m".
                              format(eachfile)))
                os.remove(os.path.join(item[0], eachfile))

        
def search_empty_file(src):
    if not os.path.exists(src):
        logging.debug(src, "does not exist !")
        sys.exit()
    else:
        result_list = []
        for items in os.walk(os.path.abspath(src)):
            for each_file in items[2]: 
                # use try except because some of my filenames are chinese characters,encoding is not
                # well supported in python 2.7
                try:
                    if not os.path.getsize(os.path.join(items[0], each_file)):
                        # if not os.path.getsize(each_file): #initially,I made a mistake here, didn't use the full path
                        logging.debug(os.path.join(items[0], each_file))
                        result_list.append(os.path.join(items[0], each_file))
                    # os.unlink(os.path.join(items[0],each_file))
                except WindowsError:
                    continue
        return result_list


def search_filename_onpattern(directory, regex):

    user_pattern = re.compile(r'('+regex+')', re.I)
    result_list = []
    for item in os.walk(os.path.abspath(directory)):
        for eachfile in item[2]:
            if  user_pattern.search(eachfile):
                logging.debug (os.path.join(item[0],user_pattern.sub(r"\033[91m\1\033[00m",eachfile)))
                result_list.append(os.path.join(item[0],eachfile))
    return result_list
     

def search_dirname_onpattern(directory, regex):
    user_pattern = re.compile(r'('+regex+')', re.I)
    result_list = []
    for item in os.walk(os.path.abspath(directory)):
        for eachdir in item[1]:
            if  user_pattern.search(eachdir):
                logging.debug(os.path.join(item[0], user_pattern.sub(r"\033[91m\1\033[00m",eachdir)))
                result_list.append(os.path.join(item[0], eachdir))
    return  result_list               


def count_file_onextension(directory):
    if not os.path.exists(os.path.abspath(directory)):
        logging.debug (directory + "does not exist")
    else:
        counter = collections.Counter()
        for path, dirs, files in os.walk(os.path.abspath(directory)):
            counter.update([os.path.splitext(eachfile)[1] for eachfile in files])
        pprint.pprint(dict(counter))
        return counter

