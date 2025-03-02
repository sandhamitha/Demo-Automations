from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import datetime
import fitz
import re

# Extract Data from a Extenal Source 
def extract_gender(pdf_path):
    doc = fitz.open(pdf_path)
    
    for page in doc:
        text = page.get_text()

        if "Male" in text or "male" in text:
            return "male"
        elif "Female" or "female" in text:
            return "female"
        elif "Rather not say" or "rather not say" in text:
            return "rather not say"
    
    return "unknown"

pdf_path = "e:/Intern Testings (TJH)/JA Process Automation/test.pdf" # attached in the repo
gender = extract_gender(pdf_path)
print(f"Extracted gender is: {gender}")


with webdriver.Chrome() as driver:
    driver.get("https://selenium-practice.netlify.app/")    
    
    time.sleep(2) # wait for page to load
    
    name_input = driver.find_element(By.XPATH, '//*[@id="name"]')
    name_input.send_keys("test")

    selection_input = driver.find_element(By.XPATH, '//*[@id="selection"]')
    select = Select(selection_input)
    select.select_by_visible_text("item 1")

    #for i in range()
    # driver.find_element(By.XPATH, ).click()
    gender_xpaths = {
        "male": '//*[@id="check1"]/option[1]',
        "female": '//*[@id="check2"]/option[2]',        
        "rather not say": '//*[@id="check3"]/option[3]'
    }

    if gender and gender in gender_xpaths:
        driver.find_element(By.XPATH, gender_xpaths[gender]).click()
    else:
        print("Gender not found")

    date_input = driver.find_element(By.XPATH, '//*[@id="date"]')
    date_input.click()
    date_input.send_keys(datetime.date.today().strftime("%d/%m/%Y"))

    submit_button = driver.find_element(By.XPATH, '/html/body/form/button')
    submit_button.click()

    time.sleep(5)

