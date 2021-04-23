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

new_status = api.update_status(input("New status: "))
img_obj = api.media_upload(input("Image path: "))
new_status_with_img = api.update_status(
    input("New status (with image): "), media_ids=[img_obj.media_id_string]
)
