#!/usr/bin/python
# created by sfzhang @2016.10.19

""" 
this program ask user's credentials and check database for his homedir
"""

import crypt
import getpass
import spwd
import pwd
import grp

def get_user_homedir():
    input_uname = raw_input("please gimme your username:")
    input_pword = getpass.getpass("please gimme your password:")
    try:
        password_hash = spwd.getspnam(input_uname.strip()).sp_pwd
        if crypt.crypt(input_pword.strip(),password_hash) == password_hash:
            homedir = pwd.getpwnam(input_uname).pw_dir
            print(input_uname+" homedir is "+homedir)
        else:
            print("you pasword is not correct!!")
    except KeyError:
        print("username does not exist!!")#incase getpanam and getspnam return keyError

if __name__ == "__main__":
    get_user_homedir()
