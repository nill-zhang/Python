# print all the config files under /etc directory
# by sfzhang
'''warnings: you may have different results due to that user's
   permission under which you execute this script, if that user
   is in the wheel group, you can issue sudo python ./extractConf.py
   to execute this script in that user's shell.
'''
import os,fnmatch
for i in os.walk('/etc'):
    for j in i[2]:
        if fnmatch.fnmatch(j,'*.conf') or fnmatch.fnmatch(j,'*.cfg') or fnmatch.fnmatch(j,'*.cnf'):
            # omit symbolic links to match find /etc -type f -iname '*.conf|*.cfg|*.cnf'
            if not os.path.islink(os.path.join(i[0],j)):
                print os.path.join(i[0],j)
            
