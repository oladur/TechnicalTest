import os
import time
from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://serene-mountain-14043.herokuapp.com/')

# Validate a Correct postcode
postCode = driver.find_element_by_xpath('//*[@id="searchLocation"]/input')
postCode.send_keys('W6 0NW')

searchPostcode = driver.find_element_by_css_selector('#searchLocation > button').submit()

time.sleep(3)
driver.refresh()

# Validate a incorrect postcode
postCode = driver.find_element_by_xpath('//*[@id="searchLocation"]/input')
postCode.send_keys('B99 9AA')

searchPostcode = driver.find_element_by_css_selector('#searchLocation > button').submit()

time.sleep(2)
driver.refresh()

# Validate an incorrect postcode with starting with two alphabets
postCode = driver.find_element_by_xpath('//*[@id="searchLocation"]/input')
postCode.send_keys('EC1A 1BB')

searchPostcode = driver.find_element_by_css_selector('#searchLocation > button').submit()

time.sleep(2)
driver.refresh()

# Validate a no postcode entry
postCode = driver.find_element_by_xpath('//*[@id="searchLocation"]/input')
postCode.send_keys('')

searchPostcode = driver.find_element_by_css_selector('#searchLocation > button').submit()












