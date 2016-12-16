#!/usr/bin/python
# by sfzhang 2016.12.15
import requests
import urllib.request
import urllib
import robobrowser
"""
four ways to submitting forms to a website
"""

def urllib_get(target_url):
    print("[urllib_get]")
    query_str = urllib.parse.urlencode({"q": "谙"})  # encode no-ascii character with utf-8
    result = urllib.request.urlopen(target_url+ '?' + query_str)
    return result.read().decode("utf-8")


def urllib_post(target_url):
    print("[urllib_post]")
    value = {"q": "谙"}
    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")
    result = urllib.request.urlopen(target_url, data)
    return result.read().decode("utf-8")


def requests_post(target_url):
    print("[requests_post]")
    value = {"q": "谙"}
    result = requests.post(target_url, params=value)
    # return result.text
    return result.content.decode("utf-8")


def robobrowser_post(target_url):
    print("[robobrowser_post]")
    br = robobrowser.RoboBrowser()
    br.open(target_url)
    form = br.get_form()
    form["q"].value = "谙"
    br.submit_form(form)
    print()


if __name__ == "__main__":
    url = "http://www.chazidian.com/zi/"
    print(urllib_get(url))
    print(urllib_post(url))
    print(requests_post(url))
    # print(robobrowser_post(url)) # broken
