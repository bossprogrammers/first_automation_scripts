from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#initialize webdriver
executable_path='/Users/softwareengineer/Desktop/web_automation/chromedriver'
driver = webdriver.Chrome(executable_path)

# Expand the window
driver.maximize_window()
driver.implicitly_wait(5)

#Open the URL
driver.get("https://google.com")
search_bar = driver.find_element(By.NAME, 'q')
search_bar.clear()
search_bar.send_keys("Babul Nokrek")

#Wait for 3 sec
sleep(3)

#click search
driver.find_element(By.NAME, 'btnK').click()

print("Congratulations! Test is PASSED!")
sleep(5)
driver.quit()