from TwitterSearch import *
from collections import Counter
import pandas as pd
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['donald', 'trump']) # let's define all words we would like to have a look for
    tso.set_language('en')
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.set_count(100)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'UubTIUOSDbsaETbSm4UdYk3mk',
        consumer_secret = 'f1RgFT5UaqhxQYiYr4aoCTppNMIwJpE0zMSWkPzsu8N7bIGjnM',
        access_token = '1718802966-aC0aukGfO6v58GQe5K2z5XSirddJ22Iw2qfnFJE',
        access_token_secret = 'bbVkfnmrozQSYJRraQC7EKjcs9Pdl39OIaMkiQHQiF28F'
     )
    

    limit = 100
    count = 0
    tweets = []
    for tweet in ts.search_tweets_iterable(tso):
        count = count + 1
        print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        tweets.append(tweet['text'])
        if count > limit:
            break
    
    df = pd.DataFrame(tweets,columns=['text'])
    print('----------------')
    print(df)

    print(Counter(" ".join(df["text"]).split()).most_common(100))

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)