import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import pathlib

import selenium.webdriver


#prof = selenium.webdriver.FirefoxProfile()
opt = selenium.webdriver.FirefoxOptions()


opt.set_preference("permissions.default.image", 2)

driver = selenium.webdriver.Firefox(firefox_options=opt)

driver.get('https://reddit.com')
driver.get('https://www.google.com')
inp = driver.find_element_by_xpath('//input[@id="lst-ib"]')
inp.clear()
inp.send_keys(u'emacs python\n')

url = driver.find_element_by_xpath('//cite[@class="iUh30"]')

driver.get(url.text)

for url in urls:
    print(url)


driver.get('https://blog.fefe.de')
driver.get('https://reddit.com')
driver.get('https://news.ycombinator.com')
driver.get('https://marktplaats.nl')


# accept cookies
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/input[2]').click()

inpt = driver.find_element_by_xpath('//*[@id="input"]')
inpt.clear()
inpt.send_keys(u'computer\ue007')

postcode = driver.find_element_by_xpath('//input[@name="postcode"]')
postcode.clear()
postcode.send_keys(u'9905')

submit = driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()
# path to the firefox binary inside the Tor package

binary = '/dev/shm/'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)


browser = None


def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser


if __name__ == "__main__":
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print("getting", url_name, "at", url)
        browser.get(url)
