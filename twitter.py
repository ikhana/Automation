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

wait = WebDriverWait(driver, 60)

# Wait for the page to load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1habvwh')))

# Wait for a random period between 60 and 90 seconds, and scroll up and down
time.sleep(random.uniform(60, 90))
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
time.sleep(random.uniform(30, 60))

# Click the next button
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
time.sleep(random.uniform(3, 7))
next_button.click()

# Fill in password
password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password_input.send_keys(your_password)

# Wait for a random period between 30 and 60 seconds
time.sleep(random.uniform(30, 60))

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
time.sleep(random.uniform(10, 20))
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
time.sleep(random.uniform(120, 180))
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {scroll_height // 2});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")

# ... (previous code remains the same)

# Search for desired topics
search_terms = ["NFT", "Metaverse"]
search_query = " OR ".join(search_terms)
search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
search_box.send_keys(search_query)
search_box.send_keys(Keys.ENTER)

# Click on the 'People' tab
people_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]')))
people_tab.click()

wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]')))


# Locate the follow buttons
follow_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="listbox"]//div[@data-testid="follow"]')))

# ... (continue with the rest of the code)

activity_duration = 2 * 60 * 60  # 2 hours
end_time = time.time() + activity_duration

num_likes = random.randint(20, 30)
num_retweets = random.randint(20, 30)
num_follows = random.randint(20, 30)

actions = ActionChains(driver)

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

while time.time() < end_time:
    for _ in range(5):
        scroll_down(driver)

    like_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="like"]')
    retweet_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="retweet"]')
    follow_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="follow"]')

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

    # Follow accounts
    for _ in range(num_follows):
        account_index = random.randint(0, len(follow_buttons) - 1)
        actions.move_to_element(follow_buttons[account_index]).click().perform()
        time.sleep(random.uniform(30, 180))

driver.quit()

