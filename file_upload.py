'''
Write a Selenium script to handle file upload functionality.

Scenario:

Open https://the-internet.herokuapp.com/upload

Upload any sample .txt file from your local system.

Validate that the file name appears after uploading.

Capture a screenshot if the upload fails.
'''
import time
import logging

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
wait_obj  = WebDriverWait(driver,10)
try:

    driver.get('https://the-internet.herokuapp.com/upload')
    logging.info('successfully launched the web browser')

    path = r'D:\PycharmProjects\automation_practise\utilities\Interview Questions.pdf'
    file_upload_element = driver.find_element('id','file-upload')
    file_upload_element.send_keys(path)
    logging.info('successfully uploaded file')

    submit_button = driver.find_element('id','file-submit')
    submit_button.click()
    logging.info('successfully submitted file')

    success_element = wait_obj.until(EC.visibility_of_element_located(('id','content')))
    logging.info(f'the message after submission {success_element.text}')

except Exception as e:
    logging.error(e)
    screen_shot = fr"D:\PycharmProjects\automation_practise\log\file_upload_fail_{time.strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(screen_shot)
    logging.error('failed screenshot')

finally:
    driver.quit()
    logging.info('browser closed ')
