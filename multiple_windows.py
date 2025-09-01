'''
Launch https://the-internet.herokuapp.com/windows

Click the “Click Here” link (it opens a new tab)

Switch to the new window and fetch the text “New Window”

Then switch back to the original window and fetch the text “Opening a new window”

Log/print both texts
'''

import time
import logging
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(r'D:\PycharmProjects\automation_practise\log\multiple_result.log'),
        logging.StreamHandler()]
)

def info(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        logging.info('login successfull')
    return wrapper



try:
    driver.get('https://the-internet.herokuapp.com/windows')
    logging.info('launched browser successfully')

    current_windows = driver.window_handles
    logging.info(f'currently {len(current_windows)} are opened')

    clickable_element = driver.find_element('xpath','//a[text()="Click Here"]')
    clickable_element.click()

    current_windows = driver.window_handles
    logging.info(f'currently {len(current_windows)} are opened')

    driver.switch_to.window(current_windows[1])
    logging.info('switched window to the child')

    element_on_child = driver.find_element('tag name','h3')
    logging.info(f'text in the child tab is {element_on_child.text}')

    driver.switch_to.window(current_windows[0])
    logging.info('driver switched back to parent')

    text_from_parent_ = driver.find_element('tag name','h3')
    logging.info(f'text in the parent tab is {text_from_parent_.text}')

except Exception as e:
    logging.info(e)
    time_stamp = fr'D:\PycharmProjects\automation_practise\log\windows{time.strftime('%Y%m%d_%H%M%S')}.png'
    driver.save_screenshot(time_stamp)
    logging.info('something went wrong')
finally:
    driver.quit()
    logging.info('browser closed')
