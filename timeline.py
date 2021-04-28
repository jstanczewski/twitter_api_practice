import tweepy
import webbrowser
from decouple import config

consumer_key = config("API_KEY")
consumer_secret_key = config("API_SECRET_KEY")
callback_uri = "oob"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pin_input = input("What's the pin value? ")
auth.get_access_token(user_pin_input)
api = tweepy.API(auth)
me = api.me()

my_timeline = api.home_timeline()

for status in my_timeline:
    print(status.text)
