import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


os.environ['PATH'] += r'home/bazgab/Desktop/web/selenium_drivers'
driver = webdriver.Chrome()


def get_index_page():
    driver.get('https://automationintesting.online/')
    let_me_hack_bypass = driver.find_element(By.XPATH, "//button[text()='Let me hack!']")
    let_me_hack_bypass.click()
      

def test_case_one():
    time.sleep(5)
    booking_button = driver.find_element(By.XPATH, '//button[contains(@class, "openBooking")]')
    booking_button.click()
    driver.implicitly_wait(10)
    first_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "07")]')
    second_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "10")]')
    
    action = ActionChains(driver)
    action.click_and_hold(first_element).move_to_element(second_element).release().perform()
    time.sleep(5)
    action.drag_and_drop(first_element, second_element).perform()
   
    room_name = driver.find_element(By.XPATH, '//input[contains(@class, "room-name")]')
    
get_index_page()   
test_case_one()
time.sleep(10)
driver.quit()