#/usr/bin/python
#by sfzhang 2016.12.17
from selenium import webdriver
import urllib.request
import urllib.parse
import bs4 as bs


def login(driver, t_uname, t_pword):
    """
    Automatically login to twitter account
    Note: selenium only find elements that are descendants of
          the current element, not siblings or siblings's descendants
    """

    boxes_parent = driver.find_element_by_tag_name("fieldset")
    boxes = boxes_parent.find_elements_by_tag_name("input")
    boxes[0].clear()  # this will clear any texts(if any) already in the textbox
    boxes[0].send_keys(t_uname)
    boxes[1].clear()
    boxes[1].send_keys(t_pword)
    button_parent = driver.find_element_by_class_name("clearfix")
    button = button_parent.find_element_by_tag_name("button")
    button.click()
    return driver


def sign_in(url):
    value = {"session[username_or_email]": "181715190@qq.com ",
             "session[password]": "ZSFFSzz131085"}
    data = urllib.parse.urlencode(value)
    data = data.encode()
    result = urllib.request.urlopen(url, data)
    soup = bs.BeautifulSoup(result.read(), "lxml")
    print(soup.head)


def initiate_driver(url):
    web_driver = webdriver.Chrome()
    web_driver.get(url)
    return web_driver


def create_app(driver):
    """Access the create app webpage trying to create a third-party app"""
    sign_in_button = driver.find_element_by_link_text("Sign in")
    sign_in_button.get_attribute("href")
    sign_in_button.click()
    a = login(driver, "181715190@qq.com", "ZSFFSzz131085")
    create_newapp_button = a.find_element_by_link_text("Create New App")
    create_newapp_button.click()
    #todo


def test_create_app(url):
    chrome_driver = initiate_driver(url)
    create_app(chrome_driver)


def test_login(url):
    chrome_driver = initiate_driver(url)
    create_app(chrome_driver, "181715190@qq.com", "ZSFFSzz131085")

if __name__ == "__main__":
    # sign_in("https://twitter.com/sessions")
    test_create_app("https://apps.twitter.com/")
    test_login("https://twitter.com/login")

