#!usr/bin/python
# by sfzhang 2016.12.12
from urllib.request import urlopen
from lxml import html
from zipfile import ZipFile
from io import BytesIO
import re
import requests
import os
import shutil
import sys


def generate_file_url(website_url):
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


def generate_poem_info(input_str):
    # poem_pattern =re.compile(r">.+(?=>)", re.DOTALL)
    # poem_pattern =re.compile(r">.+?(?=>)", re.DOTALL)
    poem_pattern = re.compile(r">(.+?)ZZ(.*?)\r\n.+?(?=>)", re.DOTALL)
    for each_match in re.finditer(poem_pattern, input_str):
        poet_name = each_match.group(1).strip()
        poet_author = each_match.group(2).strip()
        poet_content = each_match.group()
        yield poet_name, poet_author, poet_content


def generate_gbk_str():
    for i in generate_file_url("http://www.sczh.com/scdown.htm"):
        with open_file(i) as file:
            try:
                gbk_str = file.read().decode("gbk")
            except UnicodeDecodeError:
                gbk_str = file.read().decode("gb2312")
            finally:
                yield gbk_str


def generate_persons_name():
    for i in generate_gbk_str():
        file_characters_set = str_to_set(i)
        while file_characters_set:
            first_name = file_characters_set.pop()
            full_name = chr(0x5f20) + first_name
            print(full_name, end='\t\t\t')
            try:
                if input("Like the name?  "):
                    print("  ", end="")
                    if input("More about it?  "):
                        generate_dict_info(first_name)
                    yield full_name
            except EOFError:
                print("\n" + "*" * 189)
                raise StopIteration
            sys.stdout.write("\x1b[F")
        # for l, m, n in generate_poem_info(i):


def generate_dict_info(character):
    unicode_point = hex(ord(character)).strip("0x")
    required_url = "http://www.chazidian.com/r_zi_zd" + unicode_point
    dict_req = requests.get(required_url)
    dict_info_tree = html.fromstring(dict_req.content)
    section_info = dict_info_tree.xpath("//p/text()")
    results = [i.strip() for i in section_info if i.strip()]
    print("\r\n\033[33m" + "【 基本解释 】\033[0m")
    print(results[7])
    print("\r\n\033[33m" + "【 详细解释 】\033[0m")
    print(results[8])


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






