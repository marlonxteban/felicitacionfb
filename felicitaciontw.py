from __future__ import absolute_import, print_function

import tweepy
import json

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="OClhpgehW4i7uHQyqh61kz4a1"
consumer_secret="IfUaPkduVxxfagXJPuUwQnpRCpKX5koibc1xTr9sFOGEmD4CFS"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="69730725-LetLZ9WeGi1kr5DCdZgV25qD52ACr6ihUlAK06zla"
access_token_secret="fj7I4YOe0QJywhebpf1ayxgSQwBVFDHfhKVTj77qXR1I4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)
friends = api.me().friends
#print(json.dumps(api.me()._json, sort_keys=True, indent=4))
f = open('resp.txt', 'w')
print(api.me().timeline(), file="resp.txt")
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status(status='Updating using OAuth authentication via Tweepy!')
