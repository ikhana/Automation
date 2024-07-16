import time
import random
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from twitter_login import login_to_twitter
from twitter_search import twitter_search
from tweet_analysis import analyze_and_reply
from tweet_actions import like_tweet, retweet, reply_to_tweet
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load env variables
load_dotenv()
openai_api_key = os.getenv("OPEN_AIAPI")
your_email_or_username = os.getenv("TWITTER_USERNAME")
your_password = os.getenv("TWITTER_PASSWORD")

# Setup webdriver
service = Service("C:\Derivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://twitter.com")

# Login to twitter
wait = WebDriverWait(driver, 30)
try:
    login_to_twitter(driver, wait, your_email_or_username, your_password)
except:
    driver.quit()
    sys.exit("Failed to login")

# Search terms
search_terms = [
    "NFT", "Crypto", "Bitcoin", "Ethereum", "Blockchain", "DeFi", "Metaverse", 
    "Utility NFTs", "Hyperledger", "Web3", "Blockchain", 
    "Play to Earn", "Decentraland", "The Sandbox", "Regenerative Finance", 
    "Web3 Innovation", "Smart Contracts", "Elon Musk Web3", "DAOs", "CryptoArt", 
    "CryptoGaming", "Polygon", "Dapp", "Solana", "Staking", "Yield Farming", 
    "Liquidity Mining", "Interoperability", "Web 3.0", "IPFS", "Oracles", "Crypto Wallets"
]


# Calculate end time as current time + 8 hours
end_time = time.time() + 8*60*60

# Keep running until 8 hours have passed
while time.time() < end_time:
    # Loop to run the process for 4 iterations with 15 minutes interval
    for _ in range(4):
        # Sleep for a random duration in the current 15-minute interval
        time.sleep(random.uniform(_ * 1 * 60, (_ + 1) * 1* 60))

        # Pick a topic, search, like, retweet, and comment on a post
        tweet_text = twitter_search(driver, search_terms, wait)
        if tweet_text is not None:
            reply = analyze_and_reply(tweet_text, openai_api_key)
           
            reply_to_tweet(driver, wait,  reply)
            time.sleep(10)
            like_tweet(driver, wait, tweet_text)
            time.sleep(10)
            retweet(driver, wait)
            

        # Go back to the home page
        driver.get("https://twitter.com")
    
    # Sleep for a random duration in the range 60-70 minutes before the next hour starts
    # Sleep for a random duration in the range 15-20 minutes before the next hour starts
    time.sleep(random.uniform(5*60, 5*60))

