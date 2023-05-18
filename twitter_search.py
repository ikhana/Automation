import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def twitter_search(driver, search_terms,wait):
    # Choose a random search term
    search_term = random.choice(search_terms)
    search_terms.remove(search_term)

    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
    time.sleep(10)
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Click on the 'People' tab
    people_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]')))
    people_tab.click()
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-describedby]')))
    # Get a list of all the profile links
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

    time.sleep(10)
    profile_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[role="link"][href^="/"][tabindex="-1"]')))
    time.sleep(10)
    random_profile = random.choice(profile_links)
    random_profile.click()
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="primaryColumn"]')))


    # Wait for the profile page to load

    # Wait for the page to load
    time.sleep(5)
    time.sleep(10)

    # Click on the 'Tweets' tab
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tweets'))).click()

# Wait for the tweets to load
    time.sleep(5)
    time.sleep(10)

    # Retrieve all tweet texts
    tweet_texts = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
    time.sleep(10)

    # If any tweets were found, select a random one, print the text and return it
    if len(tweet_texts) > 0:
        random_tweet_text = random.choice(tweet_texts)
        time.sleep(10)
        tweet_text = random_tweet_text.text
        print(tweet_text)
        return tweet_text
    else:
        print("No tweets found.")
        return None
