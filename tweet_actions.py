from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
from selenium.common.exceptions import ElementClickInterceptedException


def like_tweet(driver, wait, tweet):
    # Liking a tweet
    for _ in range(10):  # Retry up to 10 times
        try:
            like_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="like"]')))
            time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
            like_button.click()
            print("Tweet liked.")
            time.sleep(random.uniform(5, 10))  # Random pause for human-like behavior
            break  # If successful, break out of the loop
        except (TimeoutException, ElementClickInterceptedException):
            print("Retrying to click on the like button...")
            time.sleep(2)  # If not, wait for 2 seconds and then try again

def retweet(driver, wait):
    # Retweeting a tweet
    for _ in range(10):  # Retry up to 10 times
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
            break  # If successful, break out of the loop
        except (TimeoutException, ElementClickInterceptedException):
            print("Retrying to click on the retweet button...")
            time.sleep(2)  # If not, wait for 2 seconds and then try again

def reply_to_tweet(driver, wait, reply):
    # Locate the reply box
    reply_box = None
    for _ in range(10):  # Retry up to 10 times
        try:
            reply_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Tweet text"]')))
            reply_box.click()
            reply_box.send_keys(reply)
            time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
            break  # If successful, break out of the loop
        except Exception as e:
            print(f"Retrying to locate and fill the reply box due to {e}...")
            time.sleep(2)  # If not, wait for 2 seconds and then try again

    if reply_box is None:
        print("Couldn't find the reply box.")
    else:
        # Click on the 'Reply' button
        for _ in range(10):  # Retry up to 10 times
            try:
                reply_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
                reply_button.click()
                break  # If successful, break out of the loop
            except Exception as e:
                print(f"Retrying to click on the 'Reply' button due to {e}...")
                time.sleep(2)  # If not, wait for 2 seconds and then try again

    time.sleep(random.uniform(10, 15))  # Random pause for human-like behavior





