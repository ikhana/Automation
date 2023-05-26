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

import random





def login_to_twitter(driver, wait, your_email_or_username, your_password):
    driver.get("https://twitter.com")
    # Login to twitter
    
    # Wait for the page to load
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1habvwh')))

    time.sleep(random.uniform(5, 10))

    # Click the login link
    login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="login"]')))
    time.sleep(random.uniform(5, 15))
    login_link.click()

    # Fill in username
    username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
    username_input.send_keys(your_email_or_username)

    time.sleep(random.uniform(10, 15))

    # Click the next button
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
    time.sleep(random.uniform(3, 7))
    next_button.click()

    # Fill in password
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password_input.send_keys(your_password)

    time.sleep(random.uniform(5, 10))

    # Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
    time.sleep(random.uniform(10, 15))
    login_button.click()

    time.sleep(random.uniform(60, 90))
    wait.until(EC.title_contains("Twitter"))
