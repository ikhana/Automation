import time
import re
import openai
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
from selenium.common.exceptions import TimeoutException
from tweet_analysis import analyze_and_reply



load_dotenv()

your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

service = Service("C:\Derivers\chromedriver_win32/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com")

wait = WebDriverWait(driver,30)

# Wait for the page to load
try:
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1habvwh')))
except TimeoutException:
    print("Page load timeout. Try again later.")
    driver.quit()
    sys.exit()

# Wait for a random period between 60 and 90 seconds, and scroll up and down
time.sleep(random.uniform(5, 10))
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {scroll_height // 2});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")

# Click the login link
try:
    login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="login"]')))
    time.sleep(random.uniform(5, 15))
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

# Wait for a random period between 30 and 60 seconds
time.sleep(random.uniform(10, 15))

# Click the next button
try:
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
    time.sleep(random.uniform(3, 7))
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

# Wait for a random period between 30 and 60 seconds
time.sleep(random.uniform(5,10))

# Click the login button
try:
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')))
    time.sleep(random.uniform(10, 15))
    login_button.click()
except TimeoutException:
    print("Cannot locate login button. Try again later.")
    driver.quit()
    sys.exit()

# Wait for the title to change
time.sleep(random.uniform(60, 90))
try:
    wait.until(EC.title_contains("Twitter"))
except TimeoutException:
    print("Login process timeout. Try again later.")
    driver.quit()
    sys.exit()

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



# Search for desired topics
search_terms = ["NFT", ]
search_query = "crypto"
search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
time.sleep(10)
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
# Increase the timeout period to 20 seconds
wait = WebDriverWait(driver, 20)


# Use presence_of_element_located() instead of visibility_of_element_located()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[role="link"][href^="/"]')))
time.sleep(10)

# Increase the timeout period to 20 seconds
wait = WebDriverWait(driver, 20)

# Use presence_of_element_located() instead of visibility_of_element_located()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[role="link"][href^="/"]')))


# Get all profile links
profile_links = driver.find_elements(By.CSS_SELECTOR, 'a[role="link"][href^="/"]')
time.sleep(10)

# Choose a random profile and click on it
random_profile = random.choice(profile_links)
random_profile.click()
time.sleep(10)

# Wait for the profile page to load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="primaryColumn"]')))

# Wait for the page to load
time.sleep(5)
time.sleep(10)

# Click on the 'Tweets' tab
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tweets'))).click()

# Wait for the tweets to load
time.sleep(5)
time.sleep(10)

# ...

# Retrieve all tweet texts
tweet_texts = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
time.sleep(10)

# Make sure to check if any tweets were found
if len(tweet_texts) > 0:
    # Select a random tweet text
    random_tweet_text = random.choice(tweet_texts)
    time.sleep(10)

    # Print the tweet text
    print(random_tweet_text.text)
else:
    print("No tweets found.")

# Select a random tweet text
random_tweet_text = random.choice(tweet_texts)

# Print the tweet text
tweet_text = random_tweet_text.text
print(tweet_text)

# Liking a tweet
try:
    like_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="like"]')))
    time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
    like_button.click()
    print("Tweet liked.")
    time.sleep(random.uniform(5, 10))  # Random pause for human-like behavior
except TimeoutException:
    print("The like button isn't available or clickable at the moment.")

# Retweeting a tweet
try:
    retweet_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="retweet"]')))
    time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
    retweet_button.click()

    # Wait for the pop-up menu to appear
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="Dropdown"]')))

    # Click on the "Retweet" option
    retweet_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Retweet"]')))
    retweet_option.click()

    print("Tweet retweeted.")
    time.sleep(random.uniform(5, 10))  # Random pause for human-like behavior
except TimeoutException:
    print("The retweet button isn't available or clickable at the moment.")


# ... (continue with GPT-3 sentiment analysis and replying to the tweet)

reply = analyze_and_reply(tweet_text, "your-openai-api-key")



#....................................


# Locate the 'Reply' button of the tweet
reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="reply"]')))
time.sleep(10)
time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
reply_button.click()

# Wait for the reply box to appear
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0RichTextInputContainer"]')))
time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
time.sleep(10)

reply_box = None
# Wait until the reply box is visible
for _ in range(10):  # Retry up to 10 times
    try:
        reply_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="textbox"]')))
        time.sleep(10)
        break  # If successful, break out of the loop
    except TimeoutException:
        time.sleep(2)  # If not, wait for 2 seconds and then try again
        time.sleep(10)

if reply_box is None:
    print("Couldn't find the reply box.")
else:
    # Enter the reply text
    time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior

    reply_box.send_keys(reply)
    time.sleep(10)
try:
    wait = WebDriverWait(driver, 10)
    send_reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButton"]')))
    time.sleep(10)
    send_reply_button.click()
    time.sleep(10)
except TimeoutException:
    print("The reply button isn't available or clickable at the moment.")

time.sleep(random.uniform(10, 15))  # Random pause for human-like behavior



driver.quit()
