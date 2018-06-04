"""Usage: pull_updates [-hbg] SITE

Use google or bing to search for most recent changes on a website

Arguments:
  SITE      website to search for

Options:
  -h --help
  -b          use Bing
  -g          use Google    
"""

import os
import sys
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
# import pathlib

import selenium.webdriver
import selenium.webdriver.support.ui

import selenium.webdriver.support.wait
from selenium.webdriver.support import expected_conditions as EC

from docopt import docopt

# prof = selenium.webdriver.FirefoxProfile()
opt = selenium.webdriver.FirefoxOptions()


opt.set_preference("permissions.default.image", 2)

driver = selenium.webdriver.Firefox(firefox_options=opt)
driver_wait = selenium.webdriver.support.wait.WebDriverWait(driver, 30)
# driver.get('https://reddit.com')


def scroll_click(xpath):
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(.3)
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
                   '&tbs=cdr:1,cd_min:2000,cd_max:2018,sbd:1')
    # first link goes to google but has full url encoded
    link = '//h3[@class="r"]/a'
    return [e.get_attribute('href')
            for e in driver.find_elements_by_xpath(link)]


# https://github.com/azzamsa/awesome-lisp-companies
# https://github.com/azzamsa/awesome-cl-software

def bing(name):
    #name = 'site:' + term
    for i in ['1', '2', '3', '5_0_2400x0']:
        driver.get('https://www.bing.com/search?q=' +
                   name + '&filters=ex1:"ez' + i + '"')
        try:
            el = driver.find_element_by_xpath('//li[@class="b_no"]')
        except selenium.common.exceptions.NoSuchElementException:
            link = '//ol/li/h2/a'
            # time.sleep(1)
            wait(link)
            return [e.get_attribute('href')
                    for e in driver.find_elements_by_xpath(link)]


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
       'random-state.net',
       'opengl.org',
       'leibniz-ipht.de',
       'aip.de',
       'dlr.de',
       'esa.int',
       'eurocontrol.int',
       'acolyer.org',
       'eetimes.com',
       'verasonics.com',
       'sec.gov',
       'hightechcampus.com',
       'ibeo-as.com',
       'smartphotonics.nl',
       'brightphotonics.eu',
       'nazca-design.org',
       'jdj.mit.edu',
       'cyc.com',
       'franz.com',
       'lispworks.com',
       'sbcl.org',
       'weitz.de',
       'crunchbase.com',
       'image-sensors-world.blogspot.com',
       'reddit.com',
       'digg.com',
       'nLIGHT.net',
       'sensetime.com',
       'www.compass-eos.com',
       'exaware.com',
       'mellanox.com',
       'optoscribe.com',
       'aeponyx.com',
       'hacklang.org']

crunchbase = ['crunchbase.com',
              'owler.com',
              'seedtable.com',
              'startupdatatrends.com',
              'startupgenome.com',
              'seed-db.com',
              'yclist.com',
              'cbinsights.com',
              'radar.tech.eu',
              'app.startupeuropeclub.eu',
              'angle.co',
              'mappedinisrael.com',
              'techbritain.com',
              'techlist.asia',
              'etohum.com',
              'foundedinholland.com',
              'startups.be',
              'germanystartupmap.com',
              'german-startup.de',
              'dutchstartupmap.com',
              'startupnorway.com', 'swissstartups.org']


#bing('site:' + crunchbase[23] + ' photonics')
#google('site:' + url[-1])

def marktplaats(term):
    # accept cookies
    driver.find_element_by_xpath(
        '/html/body/div/div/div[2]/form/input[2]').click()

    inpt = driver.find_element_by_xpath('//*[@id="input"]')
    inpt.clear()
    inpt.send_keys(term + '\n')

    postcode = driver.find_element_by_xpath('//input[@name="postcode"]')
    postcode.clear()
    postcode.send_keys(u'9905')

    submit = driver.find_element_by_xpath('//button[@type="submit"]')
    submit.click()


if __name__ == "__main__":
    arguments = docopt(__doc__)
    try:
        if arguments['-b']:
            for x in bing('site:' + arguments['SITE']):
                print(x)
        if arguments['-g']:
            for x in google('site:' + arguments['SITE']):
                print(x)
    except TypeError:
        print('no results', file=sys.stderr)
    driver.quit()
