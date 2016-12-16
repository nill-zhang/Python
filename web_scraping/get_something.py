#!/usr/bin/python
# by sfzhang 2016.12.15
import bs4 as bs
import urllib.request
import re


def get_explanation(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, "lxml")
    # Beautifulsoup Supports regular expression
    a_para = soup.find_all("div", {"class": re.compile(r"zi_text_content*")})
    # for item in a_para:
    #     print(item.text)
    for item in a_para:
        print("*" * 100)
        for subitem in item.strings:
            print(subitem)
    # simple_explanation = soup.find("div", {"class": re.compile(r"^zi_text.*")})
    # detailed_explanation = simple_explanation.findNext("div")
    # print(simple_explanation.text)
    # print(detailed_explanation.text)


if __name__ == "__main__":
    get_explanation("http://www.chazidian.com/r_zi_zd8c19/")

