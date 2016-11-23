#!/usr/bin/python
# -*- coding:GB2312 -*-
import json
import pprint
import operator


def get_data():
    # the file contains Chinese Character and is saved as a utf-8 encoded file
    # if you don't specify encoding here, it will use the default encoding
    # which is cp1252, which can not decode utf-8 encoded characters and will
    # display weird signs
    # record_file = open("个人_unicode.txt", encoding="utf-16")
    # Although UTF-8 does not suffer from endianness problems
    # many Windows programs (i.e. Notepad) prepend the contents of UTF-8-encoded files with BOM,
    # to differentiate UTF-8 encoding from other 8-bit encodings
    # The following file is converted to utf-8-nobom from notepad generated utf-8 file
    record_file = open("个人_utf_8_nobom.txt", encoding="utf-8")
    # record_file = open("个人_utf_8.txt", encoding="utf-16")
    # record_file = open("个人_unicode.txt", encoding="utf-16")

    print(record_file.encoding)
    # record_dict = json.load(record_file)
    # pprint.pprint(record_file.read())
    try:
        record_dict = json.load(record_file)
    except json.JSONDecodeError as ep:
        print("can not load jason file!!", ep)

    # If no exception happens
    else:
        pprint.pprint(record_dict, indent=4, width=200)
        try:
            hometown = record_dict["hometown"]
        except KeyError:
            print("can not find key in record_dict")
        stock_list = record_dict["stocks"]
        two_item = operator.itemgetter('price', 'name')
        highest_stock = max(two_item(i) for i in stock_list)
        print("Stock with the highest price:")
        print("StockName: {1} StockPrice: {0}".format(*highest_stock))

        print("My stock holdings(Ascending):")
        for stock_item in sorted(stock_list, key=operator.itemgetter('holding')):
            print(stock_item['name'].rjust(20),
                  repr(stock_item['holding']).ljust(20),
                  sep='\t')

        print("\nMy stock prices(Ascending):")
        # Another way to use the key function
        for stock_item in sorted(stock_list, key=lambda x: x['price']):
            print(stock_item['name'].rjust(20),
                  repr(stock_item['price']).ljust(20),
                  sep='\t')

        # An exception will be raised here, which will be catched in the main function
        nonsense = record_dict["age"]/0
        print(nonsense)

    # This clause will always be executed
    finally:
        record_file.close()


if __name__ == "__main__":
    try:
        get_data()
    except Exception as e:
        print("Exception encountered in get_data()", e)
