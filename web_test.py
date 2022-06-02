from this import d
from selenium import webdriver
import time 

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
print("WebDriver and WebBrowser initialized ...")
driver.get("http://127.0.0.1:5000")

time.sleep(2)

task = driver.find_element_by_xpath('/html/body/div/a[1]')
task.send_keys("Task 1")
add = driver.find_element_by_xpath('/html/body/div/a[2]')
add.click()

time.sleep(2)


