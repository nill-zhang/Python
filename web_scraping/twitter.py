#/usr/bin/python
#by sfzhang 2016.12.17
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import bs4 as bs



def get_api(url):
    driver = webdriver.Chrome()
    driver.get(url)
    #element = driver.find_element_by_link_text("Create New App")
    #element = driver.find_element_by_class_name("btn btn")
    element = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
    #element.clear()
    element.send_keys("181715190@qq.com")
    element = driver.find_element_by_xpath("//input[@name='session[password]']")
    #element.clear()
    element.send_keys("ZSFFSzz131085")
    element.send_keys(Keys.RETURN)
    element.find_element_by_tag_name("button").click()

    assert "alex" in driver.title
    print(driver.page_source)


def sign_in(url):
    value = {"session[username_or_email]": "181715190@qq.com ",
             "session[password]": "ZSFFSzz131085"}
    data = urllib.parse.urlencode(value)
    data = data.encode()
    result = urllib.request.urlopen(url, data)
    soup = bs.BeautifulSoup(result.read(), "lxml")
    print(soup.head)


if __name__ == "__main__":
    # sign_in("https://twitter.com/sessions")
    get_api("https://twitter.com/login")

