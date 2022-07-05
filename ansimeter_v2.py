# -*- coding: utf-8 -*-
"""Ansimeter V2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RSTiNMNccg4vEJz-CQ1Am3zMtHlp93R-

# Crawling Twitter
"""

# !pip install tweepy
# !pip install pandas

import tweepy
import csv

def crawlingTweet (search_key):
  api_key = 'I9jb87R9o3qso3Q00eSDbTgFA'
  api_key_secret = 'nDTQ37BfuoOBWFDYX6AGJkwC5jomH6DY3exiH2WgPkq27JIvme'
  access_token = '823304486-of2MCSFvOYF9egESWl1uD0cIvSeoANZ7iT7kYlNO'
  access_token_secret = 'nyVeJlvIKO7qkQM7JLMzrF1iaYXwMUOh28JB8ZgR24I67'
  tweetsPerQry = 10
  maxTweets = 100
  maxId = -1
  tweetCount = 0

  authentication = tweepy.OAuthHandler(api_key, api_key_secret)
  authentication.set_access_token(access_token, access_token_secret)
  api = tweepy.API(authentication, wait_on_rate_limit=True)

  while tweetCount < maxTweets:
      if maxId <= 0 :
          newTweets = api.search_tweets(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended")

      newTweets = api.search_tweets(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended", max_id=str(maxId-1))
      resultTweets = []

      if not newTweets :
          print("Tweet Habis")
          break

      for tweet in newTweets:
          dictTweet = {
              "date" : tweet.created_at, #.strftime("%m/%d/%Y, %H:%M:%S")
              "username" : tweet.user.name,
              "tweet" : tweet.full_text.encode('utf-8')
          }
          resultTweets.append(dictTweet)
          # print("{date} Username {username} : {tweet}".format(date=dictTweet["date"], username=dictTweet["username"], tweet=dictTweet["tweet"]))
          # with open("/content/drive/MyDrive/PA SABILLAH/"+search_key+".csv", 'a+', newline='') as csv_file:
          #     fieldNames = ["date", "username", "tweet"]
          #     writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=";",)
          #     writer.writerow(dictTweet)

      tweetCount += len(newTweets)
      maxId = newTweets[-1].id

      return resultTweets
#
# crawlingTweet('tokped')
#
# import pandas as pd
#
# path_file= '/content/drive/MyDrive/PA SABILLAH/'
# dataset = pd.read_csv(path_file + 'tokped.csv', sep=';')
# dataset.columns =['Date', 'Username', 'Tweets']
#
# dataset
#
# """# Prepocessing"""
#
# !pip install Sastrawi
#
# pip install googletrans==3.1.0a0
#
# import re
# import string
# import nltk
# nltk.download('wordnet')
# nltk.download('sentiwordnet')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('omw-1.4')
#
# from nltk.probability import FreqDist
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from nltk.corpus import wordnet as wn
# from nltk.corpus import sentiwordnet as swn
# from nltk.stem import WordNetLemmatizer
# from googletrans import Translator
#
# from gensim.parsing.preprocessing import remove_stopwords
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#
# stopwordFactory = StopWordRemoverFactory()
# stopword = stopwordFactory.create_stop_word_remover()
# stemmerFactory = StemmerFactory()
# stemmer = stemmerFactory.create_stemmer()
#
# stop_words = set(stopwords.words('english'))
# lemmatizer = WordNetLemmatizer()
#
# !pip install tweet-preprocessor
# import preprocessor as p
# p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.SMILEY, p.OPT.EMOJI)
#
# def casefolding(review):
#     review = review.replace("b'","")
#     review = review.lower()
#     return review
#
# # kalimat = '@shopee Ini gimAna udah menunggu 10 jam tp gAgAl,, yg lainnya pd cepet'
# # print('Kalimat : \n' + kalimat)
# # hasilCasefolding = casefolding(kalimat)
# # print('Hasil casefolding: \n' + hasilCasefolding)
#
# def filtering(text):
#     text = " ".join(filter(lambda x:x[0]!='(', text.split()))
#     text = " ".join(filter(lambda x:x[0]!='\\', text.split()))
#     text = " ".join(filter(lambda x:x[0]!="@", text.split()))
#     text = re.sub(r"\d+","", text)
#     text = text.translate(str.maketrans("","",string.punctuation))
#     text = text.strip()
#     return text
#
# # print('Hasil Casefolding : \n' + hasilCasefolding)
# # hasilFiltering = filtering(hasilCasefolding)
# # print('Hasil Filtering: \n' + hasilFiltering)
#
# def normalization(review):
#     path_file= '/content/drive/MyDrive/PA SABILLAH/data/'
#     kamus_slangword = eval(open(path_file + "slangwords.txt").read()) # Membuka dictionary slangword
#     pattern = re.compile(r'\b( ' + '|'.join (kamus_slangword.keys())+r')\b') # Search pola kata (contoh kpn -> kapan)
#     content = []
#     for kata in review.split(' '):
#         filteredSlang = pattern.sub(lambda x: kamus_slangword[x.group()],kata) # Replace slangword berdasarkan pola review yg telah ditentukan
#         content.append(filteredSlang.lower())
#     review = ' '.join(content)
#
#     return review
#
# # print('Hasil Filtering : \n' + hasilFiltering)
# # hasilNormalization = normalization(hasilFiltering)
# # print('Hasil Normalisasi: \n' + hasilNormalization)
#
# def translate(text):
#   translator = Translator()
#   translation = translator.translate(text, src='id', dest='en')
#
#   return translation.text
#
# kata_depan_list = ['no', 'not', 'nix', 'never', 'nay']
# def removeStopwords(text):
#   # for word in text.split():
#   #   if word in kata_depan_list:
#   #     return word
#   #   if word not in stop_words
#   text = [word for word in text.split() if word in kata_depan_list or word not in stop_words]
#   # for word in text.split():
#   #   print(word)
#
#   return text
#
# # removeStopwords("this is how it's been waiting for hours but failed others on not fast")
#
# # print('Hasil Normalisasi : \n' + hasilNormalization)
# # hasilTranslate = translate(hasilNormalization)
# # print('Hasil Translate: \n' + hasilTranslate)
#
# # print('Hasil Normalisasi : \n' + hasilTranslate)
# # hasilRemoveStopword = removeStopwords(hasilTranslate)
# # print('Hasil Hapus Stopword:')
# # print(hasilRemoveStopword)
#
# # x = removeStopwords('it is not Beautiful but scary')
# # print(x)
#
# def stemming(text):
#
#   text = [lemmatizer.lemmatize(word) for word in text]
#   stemmed_text = " ".join(text)
#   stemmed_text
#
#   return stemmed_text
#
# # print('Hasil Hapus Stopword:')
# # print(hasilRemoveStopword)
# # hasilStemming = stemming(hasilRemoveStopword)
# # print('Hasil stemming:')
# # print(hasilStemming)
#
# def tokenizing(review):
#     token = nltk.word_tokenize(review)
#     return token
#
# # print('Hasil Stemming : \n' + hasilStemming)
# # hasilTokenizing = tokenizing(hasilStemming)
# # print('Hasil Tokenizing:')
# # print(hasilTokenizing)
#
# def preprocessing1(text):
#
#     teks = casefolding(text)
#     teks = filtering(teks)
#
#     return teks
#
# def preprocessing2(teks):
#
#     teks = normalization(teks)
#     teks = translate(teks)
#     teks = removeStopwords(teks)
#     teks = stemming(teks)
#     tokens = tokenizing(teks)
#
#     return tokens
#
# keywords = []
# tweets = []
#
# for i, row in dataset.iterrows():
#     teks = preprocessing1(row['Tweets'])
#     tweets.append(teks)
#
# tweets = np.array(tweets)
# uniqueTweets = np.unique(tweets)
#
# notEmpty = [i for i in uniqueTweets if i]
#
# keywords=[]
# for tweet in notEmpty:
#     keyword = preprocessing2(tweet)
#     keywords.append(keyword)
#
# keywords
#
# """# POSTAGGING"""
#
# pos=neg=obj=count=0
#
# postagging = []
#
# for tweet in keywords:
#     list = tweet
#     print(list)
#     postagging.append(nltk.pos_tag(list))
#
# pos_tags = postagging
#
# pos_tags
#
# """# Sentiment Scoring"""
#
# # Convert between the PennTreebank tags to simple Wordnet tags
# def penn_to_wn(tag):
#     if tag.startswith('J'):
#         return wn.ADJ
#     elif tag.startswith('N'):
#         return wn.NOUN
#     elif tag.startswith('R'):
#         return wn.ADV
#     elif tag.startswith('V'):
#         return wn.VERB
#     return None
#
# # Returns list of pos-neg and objective score. But returns empty list if not present in senti wordnet.
# def get_sentiment(word,tag):
#     wn_tag = penn_to_wn(tag)
#
#     if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
#         return []
#
#     #Lemmatization
#     lemma = lemmatizer.lemmatize(word, pos=wn_tag)
#     if not lemma:
#         return []
#
#     #Synset is a special kind of a simple interface that is present in NLTK to look up words in WordNet.
#     #Synset instances are the groupings of synonymous words that express the same concept.
#     #Some of the words have only one Synset and some have several.
#     synsets = wn.synsets(word, pos=wn_tag)
#     if not synsets:
#         return []
#
#     # Take the first sense, the most common
#     synset = synsets[0]
#     swn_synset = swn.senti_synset(synset.name())
#
#     return [synset.name(), swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]
#
# pos=neg=obj=count=0
# senti_score = []
# kata_depan = ['no', 'not', 'nix', 'never', 'nay']
#
# for pos_val in pos_tags:
#     senti_val = [get_sentiment(x,y) for (x,y) in pos_val]
#     print(pos_val)
#     flagNegative = True
#     sum_pos=sum_neg=temp_neg=0
#     for score in senti_val:
#       try:
#           word = score[0].split('.')[0]
#           if score[3] == 1:
#             continue
#
#           elif score[1] < score[2]:
#             if flagNegative:
#               sum_pos += temp_neg * score[2]
#               flagNegative = False
#             elif word in kata_depan_list:
#               flagNegative = True
#               temp_neg = score[2]
#             else:
#               sum_neg += score[2]
#
#           elif score[1] > score[2]:
#             if(flagNegative):
#               sum_neg += temp_neg * score[1]
#               flagNegative = False
#             else:
#               sum_pos += score[1]
#
#       except:
#           continue
#     senti_score_st = sum_pos - sum_neg
#     print("-----")
#     senti_score.append(senti_score_st)
#
# senti_score
#
# def label_sentiment(sentiments):
#   sentiment_results = []
#
#   for sentiment in sentiments :
#     if sentiment > 0 :
#         sentiment_results.append("Positif")
#     elif sentiment < 0 :
#         sentiment_results.append("Negatif")
#     else :
#         sentiment_results.append("Netral")
#
#   return sentiment_results
#
# label_sentiment(senti_score)