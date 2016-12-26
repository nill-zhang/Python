#!usr/bin/python
# by sfzhang 2016.12.12
import urllib.request
import urllib.parse
from lxml import html
from zipfile import ZipFile
from io import BytesIO
import re
import requests
import os
import shutil
import sys


def generate_file_url(website_url):
    """generate website internal file urls from download page"""

    page = requests.get(website_url)
    tree = html.fromstring(page.content)
    pattern = re.compile(r"txt|zip", re.I)
    for item in tree.iter("a"):
        if re.search(pattern, item.attrib['href']):
            split_tuple = urllib.request.urlsplit(website_url)
            yield urllib.request.urljoin(split_tuple.scheme+"://"+split_tuple.netloc, item.attrib['href'])


def open_file(file_url):
    """ return file handler depending on their extension"""

    txt_pattern = re.compile(r"txt", re.I)
    zip_pattern = re.compile(r"zip", re.I)
    # You can not use arbitrary unicode strings as part of
    # an URL. Sometimes, when we have Chinese Characters in our url
    # for example, http://www.sczh.com/好.txt,
    # we need to quote them, here we don't have to
    # because its already quoted
    # head, *tail = urllib.request.urlsplit(file_url)
    # file_url = head+"://"+urllib.request.quote("".join(tail))
    try:
        file = urllib.request.urlopen(file_url)
    except urllib.request.URLError as e:
        if hasattr(e, "code"):
            print("Http Error Occured %s" % e.code)
            return None
        elif hasattr(e, "reason"):
            print("URLError Occured: %s" % e.reason)
            return None
    else:
        if re.search(zip_pattern, file_url):
            contents = BytesIO(file.read())
            zip_data = ZipFile(contents)
            return zip_data.open(zip_data.namelist()[0])
        elif re.search(txt_pattern, file_url):
            return file


def generate_poem_info(input_str):
    """parse file and pick poem snippet out"""

    # poem_pattern =re.compile(r">.+(?=>)", re.DOTALL)
    # poem_pattern =re.compile(r">.+?(?=>)", re.DOTALL)
    poem_pattern = re.compile(r">(.+?)ZZ(.*?)\r\n.+?(?=>)", re.DOTALL)
    for each_match in re.finditer(poem_pattern, input_str):
        poet_name = each_match.group(1).strip()
        poet_author = each_match.group(2).strip()
        poet_content = each_match.group()
        yield poet_name, poet_author, poet_content


def generate_gbk_str():
    """read a web-file and return its decoded string"""

    for i in generate_file_url("http://www.sczh.com/scdown.htm"):

        with open_file(i) as file:
            # you can get the encoding from html itself,sometimes
            # charset = file.headers.get_content_charset()
            # charset = file.info().get_content_charset()
            try:
                gbk_str = file.read().decode("gbk")
            except UnicodeDecodeError:
                gbk_str = file.read().decode("gb2312")
            except AttributeError:
                continue
            finally:
                yield gbk_str


def generate_persons_name():
    """parse poem content, generate names one by one"""
    for i in generate_gbk_str():
        file_characters_set = str_to_set(i)
        while file_characters_set:
            first_name = file_characters_set.pop()
            full_name = chr(0x5f20) + first_name
            print(full_name, end='\t\t\t')
            try:
                if input("Like it?  "):
                    print("\t"*3, end="")
                    if input("More about it?  "):
                        generate_name_info(chr(0x1f495), first_name)
                    yield full_name
            except EOFError:
                print("\n" + "*" * 189)
                raise StopIteration
            except requests.ConnectionError:
                continue
            sys.stdout.write("\x1b[F")
        # for l, m, n in generate_poem_info(i):


def generate_name_info(sign, character):
    """single out explanation from search results about a name"""
    unicode_point = hex(ord(character)).strip("0x")
    required_url = "http://www.chazidian.com/r_zi_zd" + unicode_point
    dict_req = requests.get(required_url)
    dict_info_tree = html.fromstring(dict_req.content)
    section_info = dict_info_tree.xpath("//p/text()")
    results = [i.strip() for i in section_info if i.strip()]
    print_name_info(sign, results)


def print_name_info(frame_sign, entries):
    """print explanation"""
    title_color = ("\033[33m", "\033[0m")
    frame_color = ("\033[91m", "\033[0m")
    fst = "【 基本解释 】"
    snd = "【 详细解释 】"
    if len(entries) >= 8:
        frame = (frame_sign * 60).join(frame_color)
        edge = frame_sign.join(frame_color)
        print(frame)
        print(edge + fst.join(title_color).ljust(len(frame) - 1, frame_sign) + edge)
        print(edge + entries[7].ljust(len(frame) - 10, frame_sign) + edge)
        print(edge + snd.join(title_color).ljust(len(frame) - 1, frame_sign) + edge)
        if len(entries) >= 9:
            print(edge + entries[8].ljust(len(frame)-10, frame_sign) + edge)
            print(frame)
        else:
            print(frame)
    else:
        print("Can Not Get Details!")


def print_name():
    term_size = shutil.get_terminal_size().columns
    print("*"+" ".join(generate_persons_name()).center(term_size-2)+"*")
    print("*" * term_size)


def str_to_set(input_str):
    nonsense_pattern = re.compile(r"\W|[0-9a-z]", re.I)
    normalized_gbk_str = re.sub(nonsense_pattern, '', input_str)
    return {i for i in normalized_gbk_str}


if __name__ == "__main__":
    print_name()






