from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = raw_input("What is your username?")
pwd = raw_input("What is your password?")
driver = webdriver.Firefox()
driver.get("https://admin.uark.edu/natcgi/uwologon")
elem = driver.find_element_by_id("LDAP_UARK_ID")
elem.send_keys(user)
elem = driver.find_element_by_id("LDAP_PASSWORD")
elem.send_keys(pwd)
elem = driver.find_element_by_name("logonSB")
elem.click()
elem = driver.find_element_by_link_text('Hourly Time')
elem.click()
elem = driver.find_element_by_link_text('Time Clock')
elem.click()
elem = driver.find_element_by_xpath('/html/body/form/div[2]/input[2]')
elem.click()
elem = driver.find_element_by_xpath('/html/body/form/div[2]/input[3]')
elem.click()