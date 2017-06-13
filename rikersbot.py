import csv
import datetime
import tweepy
import random

# cron settings
# 31 6 * * * python /home/denten/rikersbot/rikersbot.py
# paths have to be explicit for cron
path = '/home/denten/rikersbot/'

# separate the credits out to keep out of github
def creds():
    with open(path + 'keys.csv', 'r') as csvfile:
        creds = csv.DictReader(csvfile, delimiter=",")
        row = creds.next()
        return row['consumer_key'], row['consumer_secret'], row['access_token'], row['access_token_secret']

# select line number at random, check against what has been twitted
def text():
    # read in the forbidden list and cast to int
    with open(path + 'forbidden.txt', 'r') as f:
        flist = f.readlines()
        forbid_list = [int(i) for i in flist]

    # open tweets get length
    with open(path + 'tweets.txt', 'r') as f:
        tweets_list = f.readlines()
        tweets_range = len(tweets_list) - 1

    # generate a random number in range
    tweet_index = random.randint(0,tweets_range)

    # roll until we get a good number
    while tweet_index in forbid_list:
        tweet_index = random.randint(0,tweets_range)
    else:
        # append to the forbidden list and return the tweet
        with open(path + 'forbidden.txt', 'a') as f:
             f.write(str(tweet_index) + '\n')

        return tweets_list[tweet_index]

def tweet(k, t):
    try:
        # shake hands and update status
        auth = tweepy.OAuthHandler(k[0], k[1])
        auth.set_access_token(k[2], k[3])
        api = tweepy.API(auth)
        api.update_status(status=t)

        # debug stuff
        # print "akey = " + k[2]
        # print "asecret = " + k[3]
        # print "token = " + k[0]
        # print "secret = " + k[1]
        # dummy write to a file instead of tweeting
        # f = open(path + 'log.txt', 'a')
        # f.write(t + '\n')

    except tweepy.error.TweepError, e:
        # consider logging errors to file
        print e.message[0]['code']
        print e.args[0][0]['code']
        pass

# logic
tweet(creds(), text())
