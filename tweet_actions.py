from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

def like_tweet(driver, wait, tweet):
    # Liking a tweet
    try:
        like_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="like"]')))
        time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
        like_button.click()
        print("Tweet liked.")
        time.sleep(random.uniform(5, 10))  # Random pause for human-like behavior
    except TimeoutException:
        print("The like button isn't available or clickable at the moment.")

def retweet(driver, wait):
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

def reply_to_tweet(driver, wait, tweet_text, reply):
    # Locate the 'Reply' button of the tweet
    reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="reply"]')))
    time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
    reply_button.click()

    # Wait for the reply box to appear
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0RichTextInputContainer"]')))
    time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior

    reply_box = None
    # Wait until the reply box is visible
    for _ in range(10):  # Retry up to 10 times
        try:
            reply_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="textbox"]')))
            break  # If successful, break out of the loop
        except TimeoutException:
            time.sleep(2)  # If not, wait for 2 seconds and then try again

    if reply_box is None:
        print("Couldn't find the reply box.")
    else:
        # Enter the reply text
        time.sleep(random.uniform(1, 3))  # Random pause for human-like behavior
        reply_box.send_keys(reply)
        time.sleep(10)
        # Retry clicking the reply button
        for _ in range(20):  # Retry up to 10 times
            try:
                wait = WebDriverWait(driver, 10)
                send_reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButton"]')))
                time.sleep(20)
                send_reply_button.click()
                time.sleep(10)
                break  # If successful, break out of the loop
            except TimeoutException:
                print("Retrying to click on the reply button...")
                time.sleep(2)  # If not, wait for 2 seconds and then try again

    time.sleep(random.uniform(10, 15))  # Random pause for human-like behavior

