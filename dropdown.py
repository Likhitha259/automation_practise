from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get('https://letcode.in/dropdowns')
driver.maximize_window()
drop_down1=driver.find_element('id','fruits')
select_obj=Select(drop_down1)
select_obj.select_by_index(1)
sleep(3)
text1=select_obj.first_selected_option.text

success_msg=driver.find_elements('xpath','//div[@class="notification is-success"]')
if len(success_msg)>0:
    print('msg displayed')
    if text1 in (success_msg[0].text):
        print(f'the final select is {text1}')
    else:
        print('not in msg')
else:
    print('msg not displayed')
