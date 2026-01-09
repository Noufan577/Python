from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

element=driver.find_element(By.XPATH, "/html/body/div/footer/div[1]/div/ul/li[3]/ul/li[7]/a")

element.click()



#driver.quit()