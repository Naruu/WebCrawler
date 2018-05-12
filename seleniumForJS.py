from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executeable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try :
    element = WebDriverWait(driver, 10).until(EC.presence _of_element_located(By.ID, "loadedButton"))
finally :
    print(driver.find_element_by_id("content").text)
    driver.close()