'''write a script to get the name of the product having prize less then $6'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options =opt)
wait_obj = WebDriverWait(driver,10)
act_obj = ActionChains(driver)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
try:
    table_to_be_used = driver.find_element('xpath','//h2[text()="Visitors"]')
    act_obj.scroll_to_element(table_to_be_used).perform()
    assert table_to_be_used.is_displayed(),"tabel is displayed"

    def to_extract_data():
        elements = driver.find_elements('xpath','//table[@id="productTable"]//tbody/tr')
        list_of_elements =[]
        for elem in elements:
            name= elem.find_element('xpath','./td[2]').text
            assert name !="","name of the product is empty"
            prize= elem.find_element('xpath','./td[3]').text
            assert prize != "", "prize of the product is empty"
            list_of_elements.append([name,prize])
        return list_of_elements

    total_data=[]
    for i in range(1,5):
        pagination_button = wait_obj.until(EC.element_to_be_clickable(('xpath',f'//a[text()="{i}"]')))
        pagination_button.click()
        total_data.extend(to_extract_data())
    # print(len(total_data))


    final_products = [row for row in total_data if float(row[-1].strip('$'))<6]
    assert len(final_products)>0,"there is no product with the prize less than 6$"
    print(final_products)

finally:
    driver.quit()
