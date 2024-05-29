import pytest
from Registration import Sign_up, Login
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

def test_Sign_up():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    time.sleep(3)
    Sign_up()
    assert "Ivan" in driver.page_source, "Имя пользователя не найдено"
    driver.quit()

def test_Login():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    time.sleep(3)
    Login()
    assert "Ivan" in driver.page_source, "Имя пользователя не найдено"
    driver.quit()
