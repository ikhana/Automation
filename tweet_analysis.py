
import openai
def analyze_and_reply(tweet_text, openai_api_key):
    openai.api_key = openai_api_key

    # Ask GPT-3 to perform sentiment analysis
    prompt = f"Analyze the sentiment of the following tweet: \"{tweet_text}\"."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60)

    # Get the sentiment
    sentiment = response.choices[0].text.strip()
    print(f"The sentiment of the tweet is {sentiment}.")

    if sentiment == "positive":
        prompt = f"The tweet is positive: \"{tweet_text}\". I want you to generate a direct reply becuase for this tweet as I will direct copying it and pasting it into content app that will automatically enter this reply to that tweet. The reply should be according to these criteri  1) It should look like more human in nature. 2) It should contain words and phrases or hashtags that will bring maximum engagment when someone see my reply. 3) It should be in appealing way that those engaging with that reply will visit my profile or follow me."
    elif sentiment == "negative":
        prompt = f"The tweet is negative: \"{tweet_text}\".I want you to generate a direct reply becuase for this tweet as I will direct copying it and pasting it into content app that will automatically enter this reply to that tweet. The reply should be according to these criteri  1) It should look like more human in nature. 2) It should contain words and phrases or hashtags that will bring maximum engagment when someone see my reply. 3) It should be in appealing way that those engaging with that reply will visit my profile or follow me."
    else:
        prompt = f"The tweet is neutral: \"{tweet_text}\". I want you to generate a direct reply becuase for this tweet as I will direct copying it and pasting it into content app that will automatically enter this reply to that tweet. The reply should be according to these criteri  1) It should look like more human in nature. 2) It should contain words and phrases or hashtags that will bring maximum engagment when someone see my reply. 3) It should be in appealing way that those engaging with that reply will visit my profile or follow me."

    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60)

    # Get the reply
    reply = response.choices[0].text.strip()
    print(f"Reply: {reply}")

    return reply