from flask import Flask
from flask import render_template
from flask import request
import flask 
import tweepy
from tweepy import OAuthHandler

from App import app

#config

CONSUMER_TOKEN='UubTIUOSDbsaETbSm4UdYk3mk'
CONSUMER_SECRET='f1RgFT5UaqhxQYiYr4aoCTppNMIwJpE0zMSWkPzsu8N7bIGjnM'

ACCESS_TOKEN = '1718802966-aC0aukGfO6v58GQe5K2z5XSirddJ22Iw2qfnFJE'
ACCESS_SECRET = 'bbVkfnmrozQSYJRraQC7EKjcs9Pdl39OIaMkiQHQiF28F'

auth = OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)

Data

class MyListener(StreamListener,sdata):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                sdata = data
                return True
        except BaseException as e:
            print("Error on_data",str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

@app.route("/")
def index():
	auth = OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
	api = tweepy.API(auth)
	return render_template('tweets.html', tweets= tweepy.Cursor(api.user_timeline))

@app.route("/stream")
def stream():
	auth = OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	twitter_stream = Stream(auth, MyListener(data))
	twitter_stream.filter(track=['#python'])

	return data

'''
CALLBACK_URL = 'http://localhost:5000/verify'
session = dict()
db = dict() #you can save these values to a database

@app.route("/")
def send_token():
	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, 
		CONSUMER_SECRET, 
		CALLBACK_URL)

	try: 
		#get the request tokens
		redirect_url= auth.get_authorization_url()
		session['request_token']= (auth.request_token.key,
			auth.request_token.secret)
	except tweepy.TweepError:
		print 'Error! Failed to get request token'

	#this is twitter's url for authentication
	return flask.redirect(redirect_url)	

@app.route("/verify")
def get_verification():

	#get the verifier key from the request url
	verifier= request.args['oauth_verifier']

	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
	token = session['request_token']
	del session['request_token']

	auth.set_request_token(token[0], token[1])

	try:
		    auth.get_access_token(verifier)
	except tweepy.TweepError:
		    print 'Error! Failed to get access token.'

	#now you have access!
	api = tweepy.API(auth)

	#store in a db
	db['api']=api
	db['access_token_key']=auth.access_token.key
	db['access_token_secret']=auth.access_token.secret
	return flask.redirect(flask.url_for('start'))

@app.route("/start")
def start():
	#auth done, app logic can begin
	api = db['api']

	#example, print your latest status posts
	return flask.render_template('tweets.html', tweets=api.user_timeline())
'''
