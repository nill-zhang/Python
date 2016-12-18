#!/usr/bin/python
# by sfzhang 2016.12.17
import urllib.request
import bs4 as bs
import os


def store_urls(urls):
    """download html files and generate file absolute path"""
    for url in urls:
        fname = '_'.join(urllib.request.urlsplit(url)) + ".html"
        fname = fname.replace("/", "_")
        try:
            fn, _ = urllib.request.urlretrieve(url, filename=fname)
        except urllib.request.URLError:
            print("Can not download %s" % url)
            continue
        except ValueError:
            print("Not a valid url %s" % url)
            continue
        print("{:.<140}{:.>25}".format(url, "\033[33m【downloaded】\033[0m"))

        yield os.path.join(os.getcwd(), fn)


def generate_href(link):
    """extract hyperlinks from a tags in an html file"""
    with open(link, encoding="utf-8") as source:
        print(source.encoding)
        soup = bs.BeautifulSoup(source.read(), "lxml")
        for tag_a in soup.find_all("a"):
            try:
                yield tag_a["href"]
            except KeyError:
                continue

if __name__ == "__main__":
    local_htmls= store_urls(["https://en.wikipedia.org/wiki/Kevin_Bacon"])
    for i in local_htmls:
        print(i)
        print(*generate_href(i), sep="\n")






