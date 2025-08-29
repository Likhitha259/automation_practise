'''Write a script to scroll down till the end of a webpage and capture all product names.'''

import logging
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://www.agoda.com/')

wait_obj= WebDriverWait(driver,10)

#To close the popup
try:
    close_btn = driver.find_element('xpath','//button[@aria-label="Close"]')
    close_btn.click()
    logging.info('popup closed')
except:
    pass

try:
    #To select Flight
    flight_button = driver.find_element('xpath','//h6[text()="Flights"]')
    flight_button.click()
    logging.info('fetched the flight icon and clicked on it')

    # To enter onboarding
    flying_from = wait_obj.until(EC.visibility_of_element_located(('xpath','//input[@placeholder="Flying from"]')))
    flying_from.send_keys('Banglore')
    wait_obj.until(EC.visibility_of_element_located(('xpath','(//span[@class="Suggestion__text"])[2]'))).click()
    logging.info("'data for flying _from:{flying_from.get_attribute('value')} entered")

    # To enter departure
    flying_to = driver.find_element('xpath','//input[@placeholder="Flying to"]')
    flying_to.send_keys('delhi')
    wait_obj.until(EC.visibility_of_element_located(('xpath', '(//li[@class="Suggestion__categoryName_item"])[2]'))).click()
    logging.info(f"data for flying _to:{flying_to.get_attribute('value')} entered")

    # To enter date of onboarding
    departure = wait_obj.until(EC.visibility_of_element_located(('xpath','//div[@data-element-name="flight-departure"]')))
    departure.click()
    date_of_departure =departure.find_element('xpath','//span[@data-selenium-date="2025-08-30"]')
    date_of_departure.click()
    date =departure.find_element('xpath','//div[@data-selenium="date-selector-title"]')
    logging.info(f"data for departure:{date.text} entered")

    # To submit the details
    submit_button = driver.find_element('xpath','//span[text()="SEARCH FLIGHTS"]')
    submit_button.click()
    logging.info('data submit successful')

    # To count number of flights available
    # 1st method
    '''
    initial_height = driver.execute_script("return document.body.scrollHeight;")
    while True:
        driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(2)
        current_height = driver.execute_script('return document.body.scrollHeight')
        if initial_height == current_height:
            break
        initial_height = current_height
    all_flights = driver.find_elements('xpath','//button[@aria-label="Expand flight details"]')
    print(len(all_flights))
    '''
    # To count number of flights available
    # 2nd method

    initial_count=0
    while True:
        driver.execute_script("window.scrollBy(0,800);")
        time.sleep(5)
        flight_prize = driver.find_elements('xpath', '//p[@class="sc-hLseeU Typographystyled__TypographyStyled-sc-1uoovui-0 bKjorE iYbjBz"]/ancestor::div[@data-testid="flightCard-flight-detail"]/descendant::span[@class="sc-hLseeU Typographystyled__TypographyStyled-sc-1uoovui-0 bKjorE gPcWqz"]')
        flight_name = driver.find_elements('xpath','//p[@class="sc-hLseeU Typographystyled__TypographyStyled-sc-1uoovui-0 bKjorE iYbjBz"]')
        if len(flight_prize)==initial_count:
            break
        initial_count=len(flight_name)
        driver.execute_script("window.scrollBy(0,1400);")

    print(initial_count)
    for flight in range(len(flight_prize)):
        print(f'{flight_name[flight].text}--{flight_prize[flight].text}')


except Exception as e:
    print(e)

finally:
    driver.quit()