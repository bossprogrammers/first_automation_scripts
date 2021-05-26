from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#initialize webdriver
driver = webdriver.Chrome(executable_path='/Users/softwareengineer/Desktop/web_automation/chromedriver')
# Expand the window
driver.maximize_window()
#Wait 5 seconds
driver.implicitly_wait(5)
#Open the URL
driver.get("https://amazon.com")
search_field = driver.find_element(By.NAME, 'field-keywords')

search_field.send_keys("Chairs")
driver.find_element(By.ID, 'nav-search-submit-button').click()

#Verification
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(f'Actual result: {actual_result}')
expected_result = '"Chairs"'
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

print("Congratulations! Test is PASSED!")
sleep(5)
driver.quit()