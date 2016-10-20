#!env/bin/python2.7
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import simplejson as json
 
CONSUMER_TOKEN='UubTIUOSDbsaETbSm4UdYk3mk'
CONSUMER_SECRET='f1RgFT5UaqhxQYiYr4aoCTppNMIwJpE0zMSWkPzsu8N7bIGjnM'

ACCESS_TOKEN = '1718802966-aC0aukGfO6v58GQe5K2z5XSirddJ22Iw2qfnFJE'
ACCESS_SECRET = 'bbVkfnmrozQSYJRraQC7EKjcs9Pdl39OIaMkiQHQiF28F'


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data",str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
    api = tweepy.API(auth)

#	twitter_stream = Stream(auth, MyListener())
#	twitter_stream.filter(track=['#trump'])

#    trends = api.trends_available()
#   print(trends)
#    with open('data.json', 'a') as outfile:
#        json.dump(trends, outfile)
    print(api.me())


#config

