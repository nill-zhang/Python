#!usr/bin/python
# by sfzhang 2016.12.12
from urllib.request import urlopen
from lxml import html
from zipfile import ZipFile
from io import BytesIO
import re
import requests
import os


def get_file_url(website_url):
    page = requests.get(website_url)
    tree = html.fromstring(page.content)
    pattern = re.compile(r"txt|zip", re.I)
    for item in tree.iter("a"):
        if re.search(pattern, item.attrib['href']):
            yield os.path.join(os.path.split(website_url)[0], item.attrib['href'])


def open_file(file_url):
    txt_pattern = re.compile(r"txt", re.I)
    zip_pattern = re.compile(r"zip", re.I)
    file = urlopen(file_url)
    if re.search(zip_pattern, file_url):
        contents = BytesIO(file.read())
        zip_data = ZipFile(contents)
        return zip_data.open(zip_data.namelist()[0])
    elif re.search(txt_pattern, file_url):
        return file


def generate_poem_info():
    # poem_pattern =re.compile(r">.+(?=>)", re.DOTALL)
    # poem_pattern =re.compile(r">.+?(?=>)", re.DOTALL)
    poem_pattern = re.compile(r">(.+?)ZZ(.*?)\r\n.+?(?=>)", re.DOTALL)
    for i in get_file_url("http://www.sczh.com/scdown.htm"):
        with open_file(i) as file:
            gbk_str = file.read().decode("gbk")
            for each_match in re.finditer(poem_pattern, gbk_str):
                poet_name = each_match.group(1).strip()
                poet_author = each_match.group(2).strip()
                yield poet_name, poet_author, each_match.group()


if __name__ == "__main__":
    pass






