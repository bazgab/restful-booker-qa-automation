import os
from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r'home/bazgab/Desktop/web/selenium_drivers'
driver = webdriver.Chrome()


def get_index_page():
    driver.get('https://automationintesting.online/')
    let_me_hack_bypass = driver.find_element(By.XPATH, "//button[text()='Let me hack!']")
    let_me_hack_bypass.click()
    
    

get_index_page()
