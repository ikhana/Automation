from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def login_to_twitter(driver, wait, your_email_or_username, your_password):
    driver.get("https://x.com/i/flow/login")

    # Wait for the login page to load
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[data-testid="ocfSettingsListPrimaryText"]')))
        print("Login page loaded successfully.")
    except TimeoutException:
        print("Login page did not load.")
        return False

    # Fill in the username
    try:
        username_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        username_input.send_keys(your_email_or_username)
        print("Username entered successfully.")
        time.sleep(random.uniform(1, 3))  # Wait time after entering username
    except TimeoutException:
        print("Username input not found.")
        return False

    # Click the next button
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
        time.sleep(random.uniform(3, 7))
        next_button.click()
        print("Next button clicked.")
        time.sleep(random.uniform(1, 3))  # Wait time after clicking next
    except TimeoutException:
        print("Next button not found.")
        return False

    # Fill in the password
    try:
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_input.send_keys(your_password)
        print("Password entered successfully.")
        time.sleep(random.uniform(1, 3))  # Wait time after entering password
    except TimeoutException:
        print("Password input not found.")
        return False

    # Click the login button
    time.sleep(random.uniform(10, 15))
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Log in')]")))
        time.sleep(random.uniform(10, 15))
        login_button.click()
        print("Login button clicked.")
        time.sleep(random.uniform(1, 3))  # Wait time after clicking login
    except TimeoutException:
        print("Login button not found.")
        return False

    # Wait for the login process to complete
    try:
        wait.until(EC.title_contains("Home / X"))
        print("Login process completed successfully.")
        return True
    except TimeoutException:
        print("Login process did not complete.")
        return False
