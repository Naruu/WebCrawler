from selenium import webdriver
import time

driver = webdriver.PhantomJS(executeable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").txt)
driver.close()