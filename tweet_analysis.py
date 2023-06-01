import openai
def analyze_and_reply(tweet_text, openai_api_key):
    openai.api_key = openai_api_key

    # Ask GPT-3 to perform sentiment analysis
    prompt = f"Analyze the sentiment of the following tweet: \"{tweet_text}\"."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60)

    # Get the sentiment
    sentiment = response.choices[0].text.strip()
    print(f"The sentiment of the tweet is {sentiment}.")

    # Specify clear instructions for the reply
    if sentiment == "positive":
        prompt = f"The tweet is positive: \"{tweet_text}\". Begin your response directly with a reply that appears human-like, maximizes engagement, and motivates readers to visit my profile or follow me."
    elif sentiment == "negative":
        prompt = f"The tweet is negative: \"{tweet_text}\". Begin your response directly with a reply that appears human-like, maximizes engagement, and motivates readers to visit my profile or follow me."
    else:
        prompt = f"The tweet is neutral: \"{tweet_text}\". Begin your response directly with a reply that appears human-like, maximizes engagement, and motivates readers to visit my profile or follow me."

    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60, temperature=0.5)

    # Get the reply
    reply = response.choices[0].text.strip()
    print(f"Reply: {reply}")

    return reply
