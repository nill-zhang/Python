#!/usr/bin/env
# by sfzhang 2016.11.12
import pickle
import shelve
import getpass
import pprint


class BankAccount(object):

    def __init__(self, account, initial_amount=0.0):
        self.account = account
        self.password = getpass.getpass("Account password: ").strip()
        self.amount = initial_amount

    def deposit(self, amount):
        if amount >= 0:
            self.amount += amount

    def withdraw(self, amount):
        if amount >= 0:
            self.amount -= amount

    def inquiry(self):
        print "%s%s\n%s%s" % ('AccountNumber:'.ljust(20),
                              self.account.ljust(20),
                              'Balance:'.ljust(10),
                              str(self.amount).ljust(20))



def BankAccount_test():

    my_pickle_account = BankAccount('451902', 200.00)
    my_pickle_account.deposit(3999)
    my_pickle_account.inquiry()
    print(my_pickle_account.__dict__)
    with open("mybank_pickle.txt", "wb") as pickle_file:
        pickle.dump(my_pickle_account, pickle_file)
        pickle_file.close()
    with open("mybank_pickle.txt") as f:
        print("Picklefile Content:")
        pprint.pprint(f.readlines(), indent=3)
        f.close()
    with open("mybank_pickle.txt", "rb") as my_account_file:
        my_account = pickle.load(my_account_file)
        my_account_file.close()
    print("Restored account object from pickle: \n%s" % my_account.__dict__)
    #########################################################################
    my_shelve_account = BankAccount('113332', 48000)
    print(my_shelve_account.__dict__)
    shelve_file = shelve.open("mybank_shelve.txt")
    shelve_file['bank'] = my_shelve_account
    shelve_file.close()

    with open("mybank_shelve.txt") as f:
        print
        "Shelvefile Content:"
        pprint.pprint(f.readlines(), indent=3)
        f.close()

    my_account_file = shelve.open("mybank_shelve.txt")
    shelve_account = my_account_file['bank']
    print("restored account object from shelve: \n%s" % shelve_account.__dict__)

if __name__ == "__main__":
    BankAccount_test()







