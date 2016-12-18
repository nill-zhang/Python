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
    # first_entry = soup.find("div", {"class": re.compile(r"^zi_text.*")})
    # second_entry = simple_explanation.findNext("div")
    # print(first_entry.text)
    # print(second_entry.text)

    # (3)
    # first_entry = soup.find(class_="zi_text_content hide").text
    # second_entry = soup.find(class_="zi_text_content hide").text
    # print(first_entry)
    # print(second_entry)

    # (4)
    # soup.findAll("", {"class":"zi_text_content"}, limit=2)
    # soup.findAll(True, {"class":"zi_text_content"}, limit=2) also work, because
    # beautiful soup doesn't use exact match
    # two_entry = soup.findAll(class_=re.compile(r"zi_text_content*"), limit=2)
    # for i in two_entry:
    #        print(i.text)

    # the following will find all text that contains 详细
    # soup.find_all(text=re.compile(r"详细"))


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


def get_links(source):
    soup = bs.BeautifulSoup(source, "lxml")
    # get an attribute of a tag,you can use a["href"] as well
    # also, you can use
    # links = (x.get("href") for x in soup.find_all(lambda x: x.name == "a"))
    links = (a.get("href") for a in soup.find_all("a"))
    print(*links, sep="\n")


def get_category(source):
    soup = bs.BeautifulSoup(source, "lxml")
    ads = soup.find_all("div", "guanggao")
    title = soup.find_all("div", "title")
    listbox = soup.find_all("div", "listbox")
    print(*ads, sep="\n")
    print(*title, sep="\n")
    print(*listbox, sep="\n")
    for i in ads + title + listbox:
        print(i.get("class"))


def main():
    try:
        url = "http://www.chazidian.com/r_zi_zd8c19/"
        source1 = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError:
        print("page not found")
    except ValueError:
        print("invalid url")
    except urllib.request.URLError:
        print("no service or host available")
    try:
        source2 = requests.get(url).text
    except requests.ConnectionError:
        print("connection error")
    try:
        source3 = open("C:/User/Admin/Documents/GitHub/python_projects/flask/templates/sample.html").read()
    except FileNotFoundError:
        print("local html can not be found")
    get_text(source1)
    get_text(source2)
    get_tags(source3)
    get_links(source2)
    get_category(source1)


if __name__ == "__main__":
    main()

