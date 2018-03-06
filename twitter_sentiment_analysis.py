#!/usr/bin/env python
"""
Twitter Sentiment Analysis, a learning machine learning project
 This queries the twitter api and performs a sentiment analysis with TextBlob

 Siraj video: https://www.youtube.com/watch?v=o_OZdbCzHUA&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=2

 Created by: Kevin Ashcraft <kevin@kevashcraft.com>
 Created on: 2018-03-06
"""
import argparse
from textblob import TextBlob
import tweepy
import yaml

def main():
    args = get_arguments()
    secrets = get_secrets()
    analyze(args.query, args.count, secrets)

def get_arguments():
    parser = argparse.ArgumentParser(description='Twitter Sentiment Analysis with TextBlob')
    parser.add_argument('--query', required=True, help='The query to search for on Twitter')
    parser.add_argument('--count', type=int, default=100, help='The number of results to retrieve from the api')
    return parser.parse_args()

def get_secrets():
    with open('secrets.yaml') as f:
        secrets = yaml.safe_load(f)

    return secrets

def analyze(query, count, secrets):
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

    api = tweepy.API(auth)

    i = 0
    for tweet in tweepy.Cursor(api.search,
                               q=query,
                               count=count,
                               result_type='recent',
                               ).items(2):
    
        i += 1
        print('Tweet #{}:'.format(i))
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)


if __name__ == '__main__':
    main()

