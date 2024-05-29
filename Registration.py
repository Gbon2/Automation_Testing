from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.get("https://www.demoblaze.com/index.html")

time.sleep(3)

def Sign_up():
    button = driver.find_element('xpath', '//*[@id="signin2"]')
    button.click()
    time.sleep(2)

    username = driver.find_element('xpath', '//*[@id="sign-username"]')
    username.send_keys('Ivan')
    time.sleep(2)

    password = driver.find_element('xpath', '//*[@id="sign-password"]')
    password.send_keys('123')
    time.sleep(1)

    button2 = driver.find_element('xpath', '//*[@id="signInModal"]/div/div/div[3]/button[2]')
    button2.click()
    time.sleep(2)

    alert = Alert(driver)
    alert.accept()
    time.sleep(2)

    button_close = driver.find_element('xpath', '//*[@id="signInModal"]/div/div/div[3]/button[1]')
    button_close.click()
    time.sleep(1)

def Login():
    button_login_in = driver.find_element('xpath', '//*[@id="login2"]')
    button_login_in.click()
    time.sleep(2)
    username2 = driver.find_element('xpath', '//*[@id="loginusername"]')
    username2.send_keys('Ivan')
    time.sleep(2)
    password2 = driver.find_element('xpath', '//*[@id="loginpassword"]')
    password2.send_keys('123')
    time.sleep(1)
    button3 = driver.find_element('xpath', '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    button3.click()
    time.sleep(2)

    alert = Alert(driver)
    alert.accept()
    time.sleep(2)

    button3.click()

    button_close = driver.find_element('xpath', '//*[@id="logInModal"]/div/div/div[3]/button[1]')
    button_close.click()
    time.sleep(2)

    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    time.sleep(5)

#driver.quit()
