import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import pathlib

import selenium.webdriver
import selenium.webdriver.support.ui

import selenium.webdriver.support.wait
from selenium.webdriver.support import expected_conditions as EC

import time

# prof = selenium.webdriver.FirefoxProfile()
opt = selenium.webdriver.FirefoxOptions()


opt.set_preference("permissions.default.image", 2)

driver = selenium.webdriver.Firefox(firefox_options=opt)
driver_wait = selenium.webdriver.support.wait.WebDriverWait(driver, 30)
# driver.get('https://reddit.com')


def scroll_click(xpath):
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(1)
    element.click()
    return element


def combo_select(xpath: str, value: str):
    select_element = Select(driver.find_element_by_xpath(xpath))  # tag name
    for option in select_element.options:
        if option.get_attribute('value') == value:
            select_element.select_by_visible_text(option.text)


# close browser:
# driver.quit()

def wait(xpath):
    driver_wait.until(EC.element_to_be_clickable(
        (selenium.webdriver.common.by.By.XPATH, xpath)))


def wait_click(xpath):
    # time.sleep(.1)
    wait(xpath)
    el = driver.find_element_by_xpath(xpath)
    el.click()
    return el


def google(term):
    driver.get('https://www.google.com/ncr')
    inp = driver.find_element_by_xpath('//input[@id="lst-ib"]')
    inp.clear()
    inp.send_keys(term)
    inp.send_keys(u'\n')
    wait_click('//a[@id="hdtb-tls"]')  # Tools
    wait_click('//div[@aria-label="Any time"]')
    wait_click('//li[@id="qdr_d"]')
    if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
        wait_click('//div[@aria-label="Past 24 hours"]')
        wait_click('//li[@id="qdr_w"]')
    if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
        wait_click('//div[@aria-label="Past week"]')
        wait_click('//li[@id="qdr_m"]')
    if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
        wait_click('//div[@aria-label="Past month"]')
        wait_click('//li[@id="qdr_y"]')
    if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
        driver.get('https://www.google.com/search?q=' + term +
                   '&tbs=cdr%3A1%2Ccd_min%3A2000%2Ccd_max%3A2018')


# https://github.com/azzamsa/awesome-lisp-companies
# https://github.com/azzamsa/awesome-cl-software
name = 'site:' + 'latticesemi.com'
driver.get('https://www.bing.com/search?q=' + name)

inp = driver.find_element_by_xpath('//input[@id="lst-ib"]')
inp.clear()
inp.send_keys(term)
inp.send_keys(u'\n')
wait_click('//a[@id="hdtb-tls"]')  # Tools
wait_click('//div[@aria-label="Any time"]')
wait_click('//li[@id="qdr_d"]')
if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
    wait_click('//div[@aria-label="Past 24 hours"]')
    wait_click('//li[@id="qdr_w"]')
if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
    wait_click('//div[@aria-label="Past week"]')
    wait_click('//li[@id="qdr_m"]')
if '' != driver.find_element_by_xpath('//div[@id="topstuff"]').text:
    wait_click('//div[@aria-label="Past month"]')
    wait_click('//li[@id="qdr_y"]')


url = ['ampleon.com', 'cavendish-kinetics.com',
       'dialog-semiconductor.com',
       'nxp.com',
       'clifford.at',
       'sotun.de',
       'adacore.com',
       'nvidia.com',
       'intel.com',
       'altera.com',
       'xilinx.com',
       'analog.com',
       'ti.com',
       'color-chip.com',
       'innoviz.tech',
       'walabot.com',
       'omniradar.com',
       'vayyar.com',
       'office-s.nl',
       'zeiss.com',
       'ezono.com',
       'tass.plm.automation.siemens.com',
       'madspace.nl',
       'kraut.space',
       'lineageos.org',
       'oneplus.com',
       'gpd.hk',
       'hansdegoede.livejournal.com',
       'norvig.com',
       'snellman.net',
       'lisp.org',
       'pvk.ca',
       'kvardek-du.kerno.org',
       'latticesemi.com',
       'random-state.net']


google('site:' + url[-1])

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
