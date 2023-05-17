import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def twitter_search(driver, search_terms):
    search_term = random.choice(search_terms)
    search_terms.remove(search_term)

    search_box = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
    time.sleep(10)
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-describedby]')))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[role="link"][href^="/"]')))
    time.sleep(10)

    profile_links = driver.find_elements(By.CSS_SELECTOR, 'a[role="link"][href^="/"]')
    time.sleep(10)

    random_profile = random.choice(profile_links)
    random_profile.click()
    time.sleep(10)

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="primaryColumn"]')))
    time.sleep(15)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tweets'))).click()
    time.sleep(15)

    tweet_texts = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
    time.sleep(10)

    if len(tweet_texts) > 0:
        random_tweet_text = random.choice(tweet_texts)
        time.sleep(10)
        tweet_text = random_tweet_text.text
        print(tweet_text)
        return tweet_text
    else:
        print("No tweets found.")
        return None
