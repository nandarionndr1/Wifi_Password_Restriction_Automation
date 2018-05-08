import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/chromedriver')

driver.get("http://:sherleebaby@192.168.0.1/wlanAccess.asp")
    
driver.implicitly_wait(10) # seconds

select = Select(driver.find_element_by_name('MacRestrictMode'))

value = select.first_selected_option.get_attribute("value")

if (value == "0"):
    select.select_by_value("1")
else:
    select.select_by_value("0")
    
submit = driver.find_element_by_xpath("//input[@value='Apply']")

print("committed! "+submit.get_attribute("type"))
submit.click()
driver.close()

