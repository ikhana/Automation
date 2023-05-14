from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

your_email_or_username = os.getenv("LINKEDIN_USERNAME")
your_password = os.getenv("LNIKEDIN_PASSWORD")

service = Service("C:\Derivers\chromedriver_win32/chromedriver")

deriver = webdriver.Chrome(service=service)
deriver.get("https://www.linkedin.com/home")

deriver.find_element(By.ID, "session_key").send_keys(your_email_or_username)
deriver.find_element(By.ID, "session_password").send_keys(your_password)
deriver.find_element(By.CSS_SELECTOR, 'button[data-id="sign-in-form__submit-btn"]').click()

ac_titl = deriver.title
print(ac_titl)

expe_title = "Feed | LinkedIn"

if (ac_titl == expe_title):
    print("Test Passed")
else:
    print("Test Failed")

deriver.quit()