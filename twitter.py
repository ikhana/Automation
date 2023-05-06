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
load_dotenv()

your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

service = Service("C:\Derivers\chromedriver_win32/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com")

wait = WebDriverWait(driver, 30)

# Click the login link
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="login"]')))
time.sleep(random.uniform(5, 15))
login_link.click()

# Fill in username
username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
username_input.send_keys(your_email_or_username)

# Click the next button
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
time.sleep(random.uniform(3, 7))
next_button.click()

# Fill in password
password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password_input.send_keys(your_password)

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
time.sleep(random.uniform(5, 12))
login_button.click()

time.sleep(random.uniform(5, 15))
# Wait for the title to change
wait.until(EC.title_contains("Twitter"))

# Get the title and print it
ac_titl = driver.title
print(ac_titl)

expe_title = "(1) Home / Twitter"

if re.match(r'\(?\d*\)? Home / Twitter', ac_titl):
    print("Test Passed")
else:
    print("Test Failed")

specific_account = "MediaCellPPP"  # Replace with the desired account's username
driver.get(f"https://twitter.com/{specific_account}")

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

activity_duration = 2 * 60 * 60  # 2 hours
end_time = time.time() + activity_duration

num_likes = random.randint(20, 30)
num_retweets = random.randint(20, 30)

actions = ActionChains(driver)

while time.time() < end_time:
    for _ in range(5):
        scroll_down(driver)

    like_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="like"]')
    retweet_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="retweet"]')

    # Like tweets
    for _ in range(num_likes):
        tweet_index = random.randint(0, len(like_buttons) - 1)
        actions.move_to_element(like_buttons[tweet_index]).click().perform()
        time.sleep(random.uniform(30, 180))

    # Retweet tweets
    for _ in range(num_retweets):
        tweet_index = random.randint(0, len(retweet_buttons) - 1)
        actions.move_to_element(retweet_buttons[tweet_index]).click().perform()

        # Confirm retweet
        confirm_retweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="retweetConfirm"]')))
        confirm_retweet_button.click()      
        time.sleep(random.uniform(30, 180))

driver.quit()
