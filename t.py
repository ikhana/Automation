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
from tweet_actions import like_tweet, retweet, reply_to_tweet
from twitter_login import login_to_twitter
from twitter_search import twitter_search



load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

service = Service("C:\Derivers\chromedriver_win32/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com")

wait = WebDriverWait(driver,30)

try:
    login_to_twitter(driver, wait)
    # ...
finally:
    driver.quit()

# Wait for a random period between 120 and 180 seconds, and scroll up and down
time.sleep(random.uniform(10, 15))
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {scroll_height // 2});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")




# Search terms

search_terms = ["NFT", "Crypto", "Bitcoin", "Ethereum", "Blockchain", "DeFi", "AI", "ML", "Data Science", "Big Data", "Cloud Computing", "Cybersecurity", "IoT", "AR", "VR", "3D Printing", "Quantum Computing", "Robotics", "Drones", "Autonomous Vehicles", "Wireless Technology", "Edge Computing", "Nanotechnology", "Biotechnology", "Green Energy", "Space Technology", "Smart Cities", "Digital Marketing", "FinTech", "HealthTech", "AgriTech", "Gaming"]

tweet_text = twitter_search(driver, search_terms)



# ... (continue with GPT-3 sentiment analysis and replying to the tweet)

reply = analyze_and_reply(tweet_text, openai_api_key)



#....................................

# Now you can use these instances with your functions
like_tweet(driver, wait, tweet_text)
retweet(driver, wait)
reply_to_tweet(driver, wait, tweet_text, reply)






driver.quit()
