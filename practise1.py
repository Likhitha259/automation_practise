'''Write a script to open Flipkart, search for 'Mobiles', and print the first 5 mobile names.'''

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.flipkart.com/')
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO)

search_btn = driver.find_element('xpath','//input[@title="Search for Products, Brands and More"]')
search_btn.clear()

search_btn.send_keys('Mobiles')
logging.info('searching for mobiles')

search_btn.send_keys(Keys.ENTER)
logging.info('search entered')

product = driver.find_elements('xpath','//div[@class="KzDlHZ"]')
price = driver.find_elements('xpath','//div[@class="Nx9bqj _4b5DiR"]')

for element in range(0,5):
    logging.info(f'{element+1} {product[element].text}:{price[element].text}')


driver.quit()
logging.info('task completed successfully')