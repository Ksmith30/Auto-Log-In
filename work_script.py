from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
link = 'https://admin.uark.edu/natcgi/uwologon'
logon_button = '/html/body/div/form[1]/fieldset/table/tbody/tr[2]/td/input'
hourly_time_button = '/html/body/form/table[1]/tbody/tr[5]/td[1]/a'
time_clock_button = '/html/body/form/table[1]/tbody/tr[2]/td[1]/a'
validate_button = '/html/body/form/div[2]/input[2]'
save_button = '/html/body/form/div[2]/input[3]'


def type_into_browser_element_by_id(identification, text):
    element = browser.find_element_by_id(identification)
    element.send(keys)


def click_browser_element_by_xpath(xpath):
    element = browser.find_element_by_xpath(xpath)
    element.click()


user = raw_input("What is your username? ")
pwd = raw_input("What is your password? ")
browser.get(link)
type_into_browser_element_by_id("LDAP_UARK_ID", user)
type_into_browser_element_by_id("LDAP_PASSWORD", pwd)
click_browser_element_by_xpath(logon_button)
click_browser_element_by_xpath(hourly_time_button)
click_browser_element_by_xpath(time_clock_button)
click_browser_element_by_xpath(validate_button)
click_browser_element_by_xpath(save_button)
