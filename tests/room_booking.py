import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

os.environ['PATH'] += r'home/bazgab/Desktop/web/selenium_drivers'
driver = webdriver.Chrome()


def get_index_page():
    driver.get('https://automationintesting.online/')
    let_me_hack_bypass = driver.find_element(By.XPATH, "//button[text()='Let me hack!']")
    let_me_hack_bypass.click()
      
#Test case 1: Correct information 
#(database refreshes every 10 minutes, so it can't be run multiple times without test failing)
def test_case_one():
    driver.refresh()
    time.sleep(5)
    booking_button = driver.find_element(By.XPATH, '//button[contains(@class, "openBooking")]')
    booking_button.click()
    driver.implicitly_wait(10)
    first_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "02")]')
    second_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "04")]')
    
    action = ActionChains(driver)
    action.click_and_hold(first_element).move_to_element(second_element).release().perform()
    time.sleep(5)
    action.drag_and_drop(first_element, second_element).perform()
    #Finding elements
    room_firstname = driver.find_element(By.XPATH, '//input[contains(@class, "room-firstname")]')
    room_lastname = driver.find_element(By.XPATH, '//input[contains(@class, "room-lastname")]')
    room_email = driver.find_element(By.XPATH, '//input[contains(@class, "room-email")]')
    room_phone = driver.find_element(By.XPATH, '//input[contains(@class, "room-phone")]')
    book_button = driver.find_element(By.XPATH, '//button[contains(@class, "book-room")]')
    #Perform actions
    room_firstname.send_keys('Sample')
    room_lastname.send_keys('User')
    room_email.send_keys('sampleuser@provider.com')
    room_phone.send_keys('12345678')
    book_button.click()
    
def test_case_one_validation():
    try:
        confirmation_modal = driver.find_element(By.XPATH, '//*[contains(text(), "Booking Successful!")]')
        if (confirmation_modal.is_displayed):
            print('room_booking test case 1... -> Success.')    
    except NoSuchElementException:
        print('room_booking test case 1... -> Fail.')
 
 
# Test Case 2: Error -> Missing information from form    
def test_case_two():
    driver.refresh()
    time.sleep(5)
    booking_button = driver.find_element(By.XPATH, '//button[contains(@class, "openBooking")]')
    booking_button.click()
    driver.implicitly_wait(10)
    first_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "02")]')
    second_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "04")]')
    
    action = ActionChains(driver)
    action.click_and_hold(first_element).move_to_element(second_element).release().perform()
    time.sleep(5)
    action.drag_and_drop(first_element, second_element).perform()
    #Finding elements
    room_firstname = driver.find_element(By.XPATH, '//input[contains(@class, "room-firstname")]')
    room_lastname = driver.find_element(By.XPATH, '//input[contains(@class, "room-lastname")]')
    room_email = driver.find_element(By.XPATH, '//input[contains(@class, "room-email")]')
    room_phone = driver.find_element(By.XPATH, '//input[contains(@class, "room-phone")]')
    book_button = driver.find_element(By.XPATH, '//button[contains(@class, "book-room")]')
    #Perform actions
    room_firstname.send_keys('Sample')
    room_lastname.send_keys('User')
    room_email.send_keys('')
    room_phone.send_keys('12345678')
    book_button.click()
    
def test_case_two_validation():
    try:
        error_display = driver.find_element(By.XPATH, '//div[contains(@class, "alert-danger")]')
        if (error_display.is_displayed):
            print('room_booking test case 2... -> Success.')    
    except NoSuchElementException:
        print('room_booking test case 2... -> Fail.')    
    
# Test Case 3: Single night stay    
def test_case_three():
    driver.refresh()
    time.sleep(5)
    booking_button = driver.find_element(By.XPATH, '//button[contains(@class, "openBooking")]')
    booking_button.click()
    driver.implicitly_wait(10)
    first_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "11")]')
    second_element = driver.find_element(By.XPATH, '//button[contains(@class, "rbc-button-link") and contains(text(), "12")]')
    
    action = ActionChains(driver)
    action.click_and_hold(first_element).move_to_element(second_element).release().perform()
    time.sleep(5)
    action.drag_and_drop(first_element, second_element).perform()
    #Finding elements
    room_firstname = driver.find_element(By.XPATH, '//input[contains(@class, "room-firstname")]')
    room_lastname = driver.find_element(By.XPATH, '//input[contains(@class, "room-lastname")]')
    room_email = driver.find_element(By.XPATH, '//input[contains(@class, "room-email")]')
    room_phone = driver.find_element(By.XPATH, '//input[contains(@class, "room-phone")]')
    book_button = driver.find_element(By.XPATH, '//button[contains(@class, "book-room")]')
    #Perform actions
    room_firstname.send_keys('Sample')
    room_lastname.send_keys('User')
    room_email.send_keys('sampleuser@provider.com')
    room_phone.send_keys('12345678')
    book_button.click()
    
def test_case_three_validation():
    try:
        confirmation_modal = driver.find_element(By.XPATH, '//*[contains(text(), "Booking Successful!")]')
        if (confirmation_modal.is_displayed):
            print('room_booking test case 3... -> Success.')    
    except NoSuchElementException:
        print('room_booking test case 3... -> Fail.')


if __name__ == '__main__':
    get_index_page()
    test_case_one()
    test_case_one_validation()
    test_case_two()
    test_case_two_validation()
    test_case_three()
    test_case_three_validation()
