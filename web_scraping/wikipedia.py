#!/usr/bin/python
# by sfzhang 2016.12.17
import urllib.request
import bs4 as bs
import os
import re
import platform

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

        # I can use yield os.path.join(os.getcwd(), fn) as well
        # ideally, should use
        yield os.path.abspath(fn)


def generate_attrs(url, attr, *args, **kwargs):
    """extract attributes from tags in an url file
       this url file can be online or local html file
    """
    if os.path.isfile(url):
        # (solution 1)
        # if os.name.lower().startswith("posix"):
        #     url = "file://" + url
        # else:
        #     url = "file:\\\\" + url

        # (solution 2)
        # if platform.platform().lower().startswith("linux"):
        #     url = "file://" + url
        # else:
        #     url = "file:\\\\" + url

        # (solution 3) Amazing!!!!!!!!
        url = "file:" + os.sep * 2 + url

    with urllib.request.urlopen(url) as source:
        soup = bs.BeautifulSoup(source.read(), "lxml")
        for tag in soup.find_all(*args, **kwargs):
            try:
                yield tag[attr]
            except KeyError:
                continue


def traverse_wikipage(base_url, extended_url=None):
    """this function is unstable, it traverse a wikipedia
       page, check whether it's a featured or good article
       and generate an entry then move to its contained links
       recursively"""
    global traversed_links
    # global featured_articles
    # global good_articles
    if extended_url is None:
        url = base_url
    else:
        url = urllib.request.urljoin(base_url, extended_url)
    source = urllib.request.urlopen(url)
    soup = bs.BeautifulSoup(source.read(), "lxml")
    try:
        title = soup.title.text
    except AttributeError:
        title = ""
    if soup.find("div", id="mw-indicator-featured-star"):
        yield "featured", title, url
        # print(title, url, sep="\t")
        # featured_articles.append((title, url))
    elif soup.find("div", id="mw-indicator-good-star"):
        yield "good", title, url
        # print(title, url, sep="\t")
        # good_articles.append((title, url))
    links = soup.find("div", {"id": "bodyContent"})\
        .findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    traversed_links.add(extended_url)
    for link in links:
        if link["href"] not in traversed_links:
            yield from traverse_wikipage(base_url, link["href"])
            # if you put traversed_links.add(extended_url) here
            # it will cause infinite recursion


def test_traverse(base_url, extended_url):
    """test function traverse"""
    # traverse_wikpage("https://en.wikipedia.org", "wiki/China")
    with open("wiki_good_articles.txt", "w") as fgood, \
            open("wiki_featured_articles.txt", "w") as ffeature:
        # pay attention to the asterisk
        for indicator, *entry in traverse_wikipage(base_url, extended_url):
            if indicator.lower().startswith("f"):
                ffeature.write("{:<40}{:<120}\n".format(*entry))
                ffeature.flush()
            else:

                fgood.write("{:<40}{:<120}\n".format(*entry))
                fgood.flush()


def test_download(urls):
    """test function store_urls and generate_attrs"""
    local_html = store_urls(urls)
    for i in local_html:
        print(i)
        print(*generate_attrs(i, "href", "a", class_="image"), sep="\n")


if __name__ == "__main__":
    # test_download(["https://en.wikipedia.org/wiki/Kevin_Bacon"])
    traversed_links = set()
    # featured_articles = []
    # good_articles = []
    test_traverse("https://en.wikipedia.org", "wiki/China")















