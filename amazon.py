from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#initialize webdriver

driver = webdriver.Chrome(executable_path='/Users/softwareengineer/Desktop/web_automation/chromedriver')

# Expand the window
driver.maximize_window()


driver.implicitly_wait(5)

#Open the URL
driver.get("https://amazon.com")

print("Congratulations! Test is PASSED!")
sleep(5)
driver.quit()