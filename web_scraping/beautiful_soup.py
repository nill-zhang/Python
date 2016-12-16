#!/usr/bin/python
# by sfzhang 2016.12.15
import bs4 as bs
import urllib.request
import re
import requests


def get_text(source):
    """different ways to get text underneath an element"""
    soup = bs.BeautifulSoup(source, "lxml")
    # Beautifulsoup Supports regular expression
    a_para = soup.find_all("div", {"class": re.compile(r"zi_text_content*")})

    for item in a_para:
        print("*" * 100)
        for subitem in item.strings:
            print(subitem)

    # Alternatives:

    # (1)
    # for item in a_para:
    #     print(item.text)

    # (2)
    # simple_explanation = soup.find("div", {"class": re.compile(r"^zi_text.*")})
    # detailed_explanation = simple_explanation.findNext("div")
    # print(simple_explanation.text)
    # print(detailed_explanation.text)

    # (3)
    # first_explanation = soup.find(class_="zi_text_content hide").text
    # second_explanation = soup.find(class_="zi_text_content hide").text
    # print(first_explanation)
    # print(second_explanation)


def get_tags(source):
    """ different ways to get your specific tags"""
    soup = bs.BeautifulSoup(source, "lxml")
    specific_tags = soup.find_all(["address", "bdo"])
    print(*specific_tags)
    print("*"*189)
    all_tags = soup.find_all(True)
    print(*map(lambda x: x.name, all_tags), sep="\t")
    print("*" * 189)
    regex_tags = soup.find_all(re.compile(r"im"))
    print(*regex_tags)


def main():
    url = "http://www.chazidian.com/r_zi_zd8c19/"
    source1 = urllib.request.urlopen(url).read()
    source2 = requests.get(url).text
    source3 = open("C:/Users/Admin/Documents/GitHub/python_projects/flask/templates/sample.html").read()
    get_text(source1)
    get_text(source2)
    get_tags(source3)


if __name__ == "__main__":
    main()

