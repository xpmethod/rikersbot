import csv
import datetime
import tweepy
import random

# cron settings
# * * 12 03 * python /home/shared-drives/litclock/cron-bot.py
# paths have to be explicit for cron
path = '/home/denten/bots/rikersbot/'

# separate the credits out to keep out of github
def creds():
    with open(path + 'keys.csv', 'r') as csvfile:
        creds = csv.DictReader(csvfile, delimiter=",")
        row = creds.next()
        return row['token'], row['secret'], row['akey'], row['asecret']

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

        # print tweet_index
        return tweets_list[tweet_index]

def tweet(k, t):
    try:
        # k stores token, secret, api key, and api secret
        auth = tweepy.OAuthHandler(k[2], k[3])
        auth.set_access_token(k[0], k[1])
        api = tweepy.API(auth)
        api.update_status(t)
        # dummy write to a file instead of tweeting
        # f = open(path + 'log.txt', 'a')
        # f.write(t + '\n')
    except tweepy.error.TweepError, e:
        # implement logging later
        # print 'failed because of %s' % e.reason
        pass

tweet(creds(), text())
