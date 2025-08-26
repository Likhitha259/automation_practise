'''Write a script to log in to a sample site (like saucedemo.com
) and validate whether the login is successful if login failed write a script
to capture a screenshot when a test case fails.'''

import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
driver = webdriver.Chrome(options=opt)

driver.maximize_window()
driver.implicitly_wait(10)

try:
    current_url_ = "https://www.saucedemo.com/"


    driver.get(current_url_)
    logging.info('getting into the url')

    username = driver.find_element('css selector','input#user-name')
    username.clear()
    username.send_keys('problem_user')
    logging.info('Entered username')


    password = driver.find_element('css selector','input#password')
    password.clear()
    password.send_keys('secret_sauce',Keys.ENTER)
    # password.send_keys(Keys.ENTER)
    logging.info('Entered password and  submitted')

    if driver.current_url.endswith('inventory.html'):
        logging.info('successfully loged in')
    else:
        filename = f'D:/PycharmProjects/automation_practise/log/fail_{time.strftime('%Y%m%d_%H%M%S')}.png'
        driver.save_screenshot(filename)
        logging.error('unable to login and screenshot saved')

except Exception as e:
    filename = fr"D:\PycharmProjects\automation_practise\log\error_{time.strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(filename)
    logging.error(f'Error :{e}')

finally:
    driver.quit()
    logging.info('successfully closed the browser')