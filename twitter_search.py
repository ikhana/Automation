import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def twitter_search(driver, search_terms, wait):
    while search_terms:
        search_term = random.choice(search_terms)
        search_terms.remove(search_term)

        for _ in range(10):
            try:
                search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
                time.sleep(10)
                search_box.send_keys(search_term)
                search_box.send_keys(Keys.ENTER)
                time.sleep(10)

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                people_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "f=user")]/div/div/span[contains(text(), "People")]')))
                people_tab.click()
                wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-describedby]')))
                break
            except Exception:
                print("Retrying search and People tab click...")
                time.sleep(2)
                continue

        for _ in range(10):
            try:
                profile_links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[role="link"][href^="/"][tabindex="-1"]')))
                wait = WebDriverWait(driver, 30)

                random_profile = random.choice(profile_links)
                random_profile.click()
                break
            except Exception:
                print("Retrying to find profile links and click...")
                time.sleep(2)
                continue

        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="primaryColumn"]')))
        time.sleep(15)

        for _ in range(10):
            try:
                tweets_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Tweets"]')))
                tweets_tab.click()
                break
            except Exception:
                print("Retrying to find and click on Tweets tab...")
                time.sleep(2)
                continue

        time.sleep(15)
        
        for _ in range(10):
            try:
                tweet_texts = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
                time.sleep(10)

                if len(tweet_texts) > 0:
                    random_tweet_text = random.choice(tweet_texts)
                    random_tweet_text.click()
                    time.sleep(10)
                    tweet_text_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetText"]')))
                    tweet_text = tweet_text_element.text
                    print(tweet_text)
                    return tweet_text
                else:
                    print("No tweets found.")
                    raise Exception("No tweets found.")
            except Exception:
                print("Retrying to find and click on tweet texts...")
                time.sleep(2)
                continue

