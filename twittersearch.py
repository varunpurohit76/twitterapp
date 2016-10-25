from TwitterSearch import *
from collections import Counter
import pandas as pd
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['jio']) # let's define all words we would like to have a look for
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
    

    limit = 1000
    count = 0
    tweets = []
    for tweet in ts.search_tweets_iterable(tso):
        count = count + 1
        print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        tweets.append(tweet['text'])
        if count > limit:
            break
    
    print('----------------')
    print(type(tweets))
    tweets = [tweet.replace('A','a') for tweet in tweets]
    tweets = [tweet.replace('B','b') for tweet in tweets]
    tweets = [tweet.replace('C','c') for tweet in tweets]
    tweets = [tweet.replace('D','d') for tweet in tweets]
    tweets = [tweet.replace('E','e') for tweet in tweets]
    tweets = [tweet.replace('F','f') for tweet in tweets]
    tweets = [tweet.replace('G','g') for tweet in tweets]
    tweets = [tweet.replace('H','h') for tweet in tweets]
    tweets = [tweet.replace('I','i') for tweet in tweets]
    tweets = [tweet.replace('J','j') for tweet in tweets]
    tweets = [tweet.replace('K','k') for tweet in tweets]
    tweets = [tweet.replace('L','l') for tweet in tweets]
    tweets = [tweet.replace('M','m') for tweet in tweets]
    tweets = [tweet.replace('N','n') for tweet in tweets]
    tweets = [tweet.replace('O','o') for tweet in tweets]
    tweets = [tweet.replace('P','p') for tweet in tweets]
    tweets = [tweet.replace('Q','q') for tweet in tweets]
    tweets = [tweet.replace('R','r') for tweet in tweets]
    tweets = [tweet.replace('S','s') for tweet in tweets]
    tweets = [tweet.replace('T','t') for tweet in tweets]
    tweets = [tweet.replace('U','u') for tweet in tweets]
    tweets = [tweet.replace('V','v') for tweet in tweets]
    tweets = [tweet.replace('W','w') for tweet in tweets]
    tweets = [tweet.replace('X','x') for tweet in tweets]
    tweets = [tweet.replace('Y','y') for tweet in tweets]
    tweets = [tweet.replace('z','z') for tweet in tweets]
    df = pd.DataFrame(tweets,columns=['text'])
    p = []
    for x in " ".join(df["text"]).split():
        if x not in ['i','we','you','they','is','a','the','in','to','for','is','rt','he','she','it','was','were','and']:# and x.startswith("#"):
                p.append(x)
    top = Counter(p).most_common(100)
        
    for i in range(0,49):
        print top[i][0]
        print top[i][1]
        print('----------------')

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)