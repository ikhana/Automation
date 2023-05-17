# twitter_login.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sys
from dotenv import load_dotenv
import random

load_dotenv()

your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

def login_to_twitter(driver, wait):
    driver.get("https://twitter.com")

    # Wait for the page to load
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1habvwh')))
    except TimeoutException:
        print("Page load timeout. Try again later.")
        driver.quit()
        sys.exit()

    # Click the login link
    try:
        login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="login"]')))
        time.sleep(random.uniform(1, 3))  # Random sleep to simulate human behavior
        login_link.click()
    except TimeoutException:
        print("Cannot locate login link. Try again later.")
        driver.quit()
        sys.exit()

    # Fill in username
    try:
        username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
        username_input.send_keys(your_email_or_username)
    except TimeoutException:
        print("Cannot locate username input. Try again later.")
        driver.quit()
        sys.exit()

    # Wait for a random period between 1 and 3 seconds
    time.sleep(random.uniform(1, 3))  # Random sleep to simulate human behavior

    # Click the next button
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
        time.sleep(random.uniform(1, 3))  # Random sleep to simulate human behavior
        next_button.click()
    except TimeoutException:
        print("Cannot locate next button. Try again later.")
        driver.quit()
        sys.exit()

    # Fill in password
    try:
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password_input.send_keys(your_password)
    except TimeoutException:
        print("Cannot locate password input. Try again later.")
        driver.quit()
        sys.exit()

    # Wait for a random period between 1 and 3 seconds
    time.sleep(random.uniform(1, 3))  # Random sleep to simulate human behavior

    # Click the login button
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
        time.sleep(random.uniform(1, 3))  # Random sleep to simulate human behavior
        login_button.click()
    except TimeoutException:
        print("Cannot locate login button. Try again later.")
        driver.quit()
        sys.exit()

    # Wait for the title to change
    try:
        wait.until(EC.title_contains("Twitter"))
    except TimeoutException:
        print("Login process timeout. Try again later.")
        driver.quit()
        sys.exit()
