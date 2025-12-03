import logging
from logging import exception
from time import sleep
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options = opt)
driver.maximize_window()
try:
    driver.get("https://admin:admin@the-internet.herokuapp.com/")
    alert_button=driver.find_element('xpath','//a[.="Basic Auth"]')
    alert_button.click()
    sleep(3)
except Exception as e:
    print(e)
