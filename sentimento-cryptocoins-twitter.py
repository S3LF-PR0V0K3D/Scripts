#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para buscar sentimento de alguma criptomoeda no twitter
Created on Tue Aug 27 12:30:07 2019

@author: Felipe Ssoares
"""

from textblob import TextBlob as tb
import tweepy
import numpy as np

consumer_key = 'jcbC0lKBQnqywKJHWjQ3N6X8H'
consumer_secret = 'dlZYpzygUwQ3c3E5okrdkbJhpc7gtphph1vGjuVgHOptxpAMQm'

access_token = '1166341851265359872-qBf2W33SuZ5lhWceu4gskyub3wWHvz'
access_token_secret = '9tFklOPejZvY5GjsKgFYUUy56bzcTJCTPtbKIdAeHJF46'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Variável que irá armazenar todos os Tweets com 
#a palavra escolhida na função search da API
pesquisa = input(
        '========= DataCrypto Analytics ========='
        '\n\nQual palavra deseja calcular o sentimento no Twitter?'
        '\n\nDigite aqui por favor:')
public_tweets = api.search(pesquisa)

tweets = [] # Lista vazia para armazenar scores
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)
    print(polarity)


print('================================='
      '\n\nA média calculada foi de: ' + str(np.mean(tweets)))


        
