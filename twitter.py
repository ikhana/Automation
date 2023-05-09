import time
import re
import sys
import os
from dotenv import load_dotenv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

load_dotenv()

your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

service = Service("C:\Derivers\chromedriver_win32/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com")

wait = WebDriverWait(driver, 10)

# Wait for the page to load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1habvwh')))

# Wait for a random period between 60 and 90 seconds, and scroll up and down
time.sleep(random.uniform(5, 10))
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {scroll_height // 2});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")

# Click the login link
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="login"]')))
time.sleep(random.uniform(5, 15))
login_link.click()

# Fill in username
username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
username_input.send_keys(your_email_or_username)

# Wait for a random period between 30 and 60 seconds
time.sleep(random.uniform(10, 15))

# Click the next button
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
time.sleep(random.uniform(3, 7))
next_button.click()

# Fill in password
password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password_input.send_keys(your_password)

# Wait for a random period between 30 and 60 seconds
time.sleep(random.uniform(10, 15))

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
time.sleep(random.uniform(10, 15))
login_button.click()

# Wait for the title to change
time.sleep(random.uniform(5, 15))
wait.until(EC.title_contains("Twitter"))

# Get the title and print it
ac_titl = driver.title
print(ac_titl)

# Check if the login test has passed
if re.match(r'\(?\d*\)? Home / Twitter', ac_titl) or "Home / Twitter" in ac_titl:
    print("Test Passed")
else:
    print("Test Failed")

# Wait for a random period between 120 and 180 seconds, and scroll up and down
time.sleep(random.uniform(10, 15))
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {scroll_height // 2});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")

# ... (previous code remains the same)

# Search for desired topics
search_terms = ["NFT", ]
search_query = " NFT "
search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
search_box.send_keys(search_query)
search_box.send_keys(Keys.ENTER)
time.sleep(10)


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
## Click on the 'People' tab
people_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]')))
people_tab.click()

# Wait for the search results to load
wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-describedby]')))

# Get a list of all the elements with 'aria-describedby' attribute
follow_buttons = driver.find_elements(By.XPATH, '//div[@aria-describedby]')

# Locate the 'a' tags corresponding to each follow button
profiles = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(), "OpenSea")]/ancestor::a | //span[contains(text(), "Bitcoin AI")]/ancestor::a')))



# Choose a random profile and click on it
random_profile = random.choice(profiles)
random_profile.click()

# Wait for the profile page to load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="primaryColumn"]')))

time.sleep(20)


driver.quit()

