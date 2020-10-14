from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get('http://envybox.io/')
assert "Envybox" in driver.page_source
login_button = driver.find_element(By.CSS_SELECTOR, "a[class='btn_room login_button']")
login_button.click()
username = driver.find_element(By.CSS_SELECTOR, "input[type='username']")
username.click()
username.send_keys('agentpnz90@gmail.com')
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.click()
password.send_keys('dzham')
enter = driver.find_element(By.CSS_SELECTOR, "a[class='enter_btn_form log-in-submit']")
enter.click()
time.sleep(2)
driver.find_element_by_class_name('profile-info')
driver.quit()
