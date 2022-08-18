from selenium import webdriver
from selenium.webdriver.common.by import By

# set chromodriver.exe path
driver = webdriver.Chrome(
    executable_path="/Users/van/Code/automation/chromedriver")
# implicit wait
driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# launch URL
driver.get("https://chat.zalo.me")
# implicit wait
driver.implicitly_wait(30)


def send_message(phone):
    # identify phone search input
    phone_input = driver.find_element(By.ID, "contact-search-input")
    # write to input
    phone_input.send_keys(phone)
    # implicit wait
    driver.implicitly_wait(5)
    # identify friend card
    friend_card = driver.find_element(
        By.XPATH, "//div[starts-with (@id, 'friend-item-')]")
    # click on card
    friend_card.click()
    # implicit wait
    driver.implicitly_wait(5)
    # identify message input field
    mess_input = driver.find_element(By.ID, "richInput")
    # write to input
    mess_input.send_keys(
        "Automated v1.0.1 - array of users, uncustomised message")
    # identify send button field
    button = driver.find_element(By.XPATH, "//div[text()='Gửi']")
    # click button
    button.click()
    # implicit wait
driver.implicitly_wait(5)


list = ["0911337845", "0903997671", "0925024229"]

for l in list:
    send_message(l)