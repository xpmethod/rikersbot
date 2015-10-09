import csv
import datetime
import tweepy

# cron settings
# * * 12 03 * python /home/shared-drives/litclock/cron-bot.py
# paths have to be explicit for cron
path = '/home/shared-drives/litclock/'

# separate the credits out to keep out of github
def creds():
    with open(path + 'creds.csv', 'r') as csvfile:
        creds = csv.DictReader(csvfile, delimiter=",")
        row = creds.next()
        return row['token'], row['secret'], row['akey'], row['asecret']

# select line number at random, check against what has been twitted
def random_text():
    # prune according to the "already tweeted" index log

    # generate a random number in the remaining range

    # pass the text of the tweet

    with open(path + 'tweets.txt', 'r') as f:
        tweets = f.readlines()

    tweet = tweets[ind]

    # append "already tweeted" to index log
    with open(path + 'log.csv', 'a') as f:
        f.write(ind + ',' + date + ',' + tweet)

    with open(path + 'creds.csv', 'r') as csvfile:
        creds = csv.DictReader(csvfile, delimiter=",")
        row = creds.next()
        return row['token'], row['secret'], row['akey'], row['asecret']

def tweet(t):

# def tweet(k, t):
#     try:
#         # k stores token, secret, api key, and api secret
#         auth = tweepy.OAuthHandler(k[2], k[3])
#         auth.set_access_token(k[0], k[1])
#         api = tweepy.API(auth)
#         api.update_status(t)
#         # dummy write to a file instead of tweeting
#         # f = open(path + 'log.txt', 'a')
#         # f.write(t + '\n')
#     except tweepy.error.TweepError, e:
#         # implement logging later
#         # print 'failed because of %s' % e.reason
#         pass
# 

tweet(creds(), text())
