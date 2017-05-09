#!/usr/bin/python
# by sfzhang 2016.11.10
import random


class RbcAccount(object):
    account_number = 0

    def __init__(self, name, balance, func):
        self.name = name
        self.balance = balance
        # self.deposit = func  # instance attribute, which takes precedence over class attribute(Rbcaccount.deposit)
        RbcAccount.account_number += 1
        print('%d accounts exist in our bank' % RbcAccount.account_number)

    def __del__(self):
        print('deleting instance')
        # RbcAccount.account_number -= 1

    def withdraw(self, amount):
        self.balance -= amount
        print('current balance after withdraw: %d' % self.balance)

    def deposit(self, amount):
        self.balance += amount
        print('current balance after deposit: %d' % self.balance)

    def inquiry(self):
        return 'name: %s, balance : %d' % (self.name, self.balance)


def custom(num):
    print("num : %d" % num)


def RbcAccount_test():
    account1 = RbcAccount('sfzhang', random.randint, custom)
    account2 = RbcAccount('xlyang', random.uniform(2, 200), custom)
    account3 = RbcAccount('lyzhang', random.randint, custom)
    account4 = RbcAccount('jchu', random.randint, custom)
    account5 = RbcAccount('qshu', random.randint, custom)
    name_list = ['Shaofeng Zhang', 'Xuelian Yang', 'Linyu Zhang', 'Ji Chu', 'Qiang Shu']
    # Instances are not generated when you define a generator, until you iterate the generator
    instance_list = (RbcAccount(item, random.uniform(0, 10000), custom) for item in name_list)
    for i in instance_list:
        print(i.inquiry())

if __name__ == "__main"__:
    RbcAccount_test()
    



