from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# set chromodriver.exe path
driver = webdriver.Chrome(
    executable_path="/Users/van/Code/automation/chromedriver")
# implicit wait
driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# launch URL
driver.get("https://gl.run")
# implicit wait
driver.implicitly_wait(30)
# Account
account = ["giaolang", "giaolang"]

#find name input + click + type
name = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
print(name)
driver.implicitly_wait(10)
name.send_keys(account[0])
driver.implicitly_wait(10)
#password
password = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
driver.implicitly_wait(10)
print(account[1])
password.send_keys(account[1])
driver.implicitly_wait(10)
# identify send button field
button = driver.find_element(By.XPATH, "//button[text()='LOGIN']")
# click button
button.click()
driver.implicitly_wait(10)

button = driver.find_element(By.CSS_SELECTOR, "span[class='ant-avatar ant-avatar-sm ant-avatar-circle']")
button.click()
driver.implicitly_wait(10)


log_out = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-hover__darken"))).click()
# print(log_out.get_attribute("style"))
# log_out.click()

# ant-avatar ant-avatar-sm ant-avatar-circle
# By.CSS_SELECTOR, "span[class='button-hover__darken']"