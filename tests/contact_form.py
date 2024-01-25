import os
from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r'home/bazgab/Desktop/web/selenium_drivers'
driver = webdriver.Chrome()


def get_index_page():
    driver.get('https://automationintesting.online/')
    let_me_hack_bypass = driver.find_element(By.XPATH, "//button[text()='Let me hack!']")
    let_me_hack_bypass.click()
      

def test_case_one():
    
    driver.implicitly_wait(10)
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    phone_field = driver.find_element(By.ID, "phone")
    subject_field = driver.find_element(By.ID, "subject")
    text_field = driver.find_element(By.ID, "description")
    submit_button = driver.find_element(By.ID, "submitContact")
   
   
    #Test Case 1: Sending Valid Info
    
    name_field.send_keys("Sample User")
    email_field.send_keys("sampleemail@provider.com")
    phone_field.send_keys("11 1234 1234")
    subject_field.send_keys("Room Inquiry")
    text_field.send_keys("This is a sample message to inquire about room availability. Please use user info to contact.")
    submit_button.click()
    # while (True):
    #     pass


def test_one_validate():
    test_input = driver.find_element(By.XPATH, "//div[@style='height: 412px;']")
    if (test_input.is_displayed):
        print('Test Case 1... -> Success')
    else:
        print('Test Case 1... -> Fail')
        
        
        
        
get_index_page()
test_case_one()
test_one_validate()        
        