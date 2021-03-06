#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import *
import json
import re
import datetime

date = datetime.date.today().strftime("%B_%d_%Y")

file_ = open(date.lower() + ".json", "a")
tweets = []

class StdOutListener(StreamListener):

    def on_data(self, data):
        if len(tweets)>100000:
            return False

        try:
            tweet = json.loads(data)

            if "created_at" in tweet:
                if tweet["lang"]=="en": 
                        if not tweet["entities"]["urls"]:
                            if not "retweeted_status" in tweet:
                                if not "media" in tweet["entities"]:
                                        if tweet["text"] > 5:
                                            if not "#MTVStars" in tweet["text"]:
                                                if not "Weather Channel" in tweet["text"]:
                                                    tweets.append(json.loads(data))
                                                    file_.write(data)
                                                    return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print status
        return True

class twitterStats():
    file_.read

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.sample()
