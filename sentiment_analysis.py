import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from TwitterSearch import *
from collections import Counter
try:
     tso = TwitterSearchOrder() # create a TwitterSearchOrder object
     tso.set_keywords(['movie review']) # let's define all words we would like to have a look for
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


     def word_feats(words):
    	return dict([(word, True) for word in words])
  
     negids = movie_reviews.fileids('neg')
     posids = movie_reviews.fileids('pos')
 
     negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
     posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
     negcutoff = len(negfeats)*1
     poscutoff = len(posfeats)*1
     trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
#naive bayes classifier trained on movie corpus dataset
     classifier = NaiveBayesClassifier.train(trainfeats)

     limit = 1000
     count = 0
     tweets = []
     for tweet in ts.search_tweets_iterable(tso):
        count = count + 1
        print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        tweets.append(tweet['text'])
	print(classifier.classify(word_feats(tweet['text'])))
        if count > limit:
            break


 




except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
