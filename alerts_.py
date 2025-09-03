'''
Open https://the-internet.herokuapp.com/javascript_alerts

Click "Click for JS Prompt"

Enter your name in the prompt, accept it.

Capture the text displayed on the page after accepting.

Log success/failure with screenshot on failure.

'''
import time
import logging
from selenium import webdriver

logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'

)

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options = opt)
driver.maximize_window()
try:
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    logging.info('launched the browser successfully')

    js_prompt_button = driver.find_element('xpath','//button[text()="Click for JS Prompt"]')
    js_prompt_button.click()
    logging.info('clicked on js prompt button')

    alert_obj = driver.switch_to.alert
    alert_obj.send_keys('RadheKrishna')
    logging.info('the value for alert has been given')

    alert_obj.accept()
    logging.info('the value has accepted')

    result = driver.find_element('id','result')
    expected_result = 'You entered: RadheKrishna'
    assert expected_result == result.text,f'expected {expected_result} but got {result.text}'
    logging.info('result matched')

except Exception as e:
    logging.error(e)
    fil =fr"D:\PycharmProjects\automation_practise\log\alert_{time.strftime('%H%M%S_%Y%m%d')}.png"
    driver.save_screenshot(fil)
    logging.info('screenshot saved for failed')

finally:
    driver.quit()
    logging.info('browser closed')

