#! python27
from __future__ import print_function
import re
import os
import sys
# class colors:
# '''Colors class:
    # reset all colors with colors.reset
    # two subclasses fg for foreground and bg for background.
    # use as colors.subclass.colorname.
    # i.e. colors.fg.red or colors.bg.green
    # also, the generic bold, disable, underline, reverse, strikethrough,
    # and invisible work with the main class
    # i.e. colors.bold
# '''
    # reset='\033[0m'
    # bold='\033[01m'
    # disable='\033[02m'
    # underline='\033[04m'
    # reverse='\033[07m'
    # strikethrough='\033[09m'
    # invisible='\033[08m'
    # class fg:
        # black='\033[30m'
        # red='\033[31m'
        # green='\033[32m'
        # orange='\033[33m'
        # blue='\033[34m'
        # purple='\033[35m'
        # cyan='\033[36m'
        # lightgrey='\033[37m'
        # darkgrey='\033[90m'
        # lightred='\033[91m'
        # lightgreen='\033[92m'
        # yellow='\033[93m'
        # lightblue='\033[94m'
        # pink='\033[95m'
        # lightcyan='\033[96m'
    # class bg:
        # black='\033[40m'
        # red='\033[41m'
        # green='\033[42m'
        # orange='\033[43m'
        # blue='\033[44m'
        # purple='\033[45m'
        # cyan='\033[46m'
        # lightgrey='\033[47m'


def search_text(directory, regex):
    if not os.path.exists(os.path.abspath(directory)):
        print(directory+" does not exist!")
    else:
        user_pattern = re.compile(r'('+regex+')', re.S)
        for item in os.walk(directory):            
            if not item[2]:
                continue
            else:
                for each_file in item[2]:                 
                    file_obj = open(os.path.join(item[0], each_file), 'r')
                    lines = file_obj.readlines()
                    flag = 0 #determine filename which contains successful matches 
                             #is printed or not,if not print, only once
                    # start = 0
                    # for each_line in lines:
                        # if user_pattern.search(each_line):
                            # if not flag: 
                                # print (os.path.join(item[0],each_file).center(80,'*'))
                                # flag = 1
                            # # print str(lines.index(each_line)+1) + " : ",\
                            # # user_pattern.sub(r"\033[92m\1\033[00m",each_line),
                            # """there is a serious bug, when you use index method, 
                               # the second and third match will all give the same 
                               # index because index always return the first match,
                               # you need to shift index scope when you done with one
                               # or you can use for i in range(len(lines)), print i
                            # """
                            # print (str(lines.index(each_line,start,)+1),\
                            # user_pattern.sub(r"\033[94m\1\033[00m",each_line),sep=":",end="")
                            # start =  lines.index(each_line,start,) + 1                            
                        # else:                          
                            # continue
                    for line_number in range(len(lines)):
                        if user_pattern.search(lines[line_number]):
                            if not flag: 
                                print(os.path.join(item[0], each_file).center(80, '*'))
                                flag = 1                          
                            print(str(line_number+1),
                                  user_pattern.sub(r"\033[91m\1\033[00m",
                                  lines[line_number].strip(' ')),
                                  sep=":",
                                  end="")
                        else:
                            continue
                    file_obj.close()

if __name__ == "__main__":
    
    search_text(sys.argv[1], sys.argv[2])
