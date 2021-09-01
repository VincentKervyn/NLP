########### BERT ###########

"""BERT (Bidirectional Encoder Representations from Transformers) is a NLP model developed by Google in 2018.
It is a model that is already pre-trained on a 2,5000M (+- 170 GB) words corpus from Wikipedia."""


import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

"""test tensoflow"""
# import tensorflow as tf
# print(tf.test.gpu_device_name())
"""test pytorc"""
# import torch.cuda
# import torch
# x = torch.rand(5, 3)
# print(x)
# print (torch.cuda.device_count() )

"""Exercice"""
odile = "dataset/odile_data.csv"
data = pd.read_csv('dataset/odile_data.csv', sep = ',')
data['sentence'] = data['sentence'].astype("string")
sentence = data['sentence']
print(type(sentence))
# print (sentence)
# profile = ProfileReport(data, title="Pandas Profiling Report",  explorative=True)
# profile.to_file(output_file="Odile.html")

""" Analyze the dataset !
# It's time to take a quick look at our data.
#
# Exercise : You must answer the following questions:
#
# How many observations does the dataset contain? 1555
# How many different labels does the dataset contain? 2
# Which labels contain the most observations? Sentence (1543)
# Which labels contain the fewest observations? intent (95)
#
# It's time to clean up !
# Not all NLP tasks require the same preprocessing. In this case, we have to ask ourselves some questions:
#
# Are there unwanted characters in the dataset? For example, do you want to keep the smiley's or not?
# If, for example, you want to create labels to analyze feelings, it might be perishable to keep the smiley's.
# Is it relevant to keep capital letters in sentences?
# In this case, capital letters don't really matter, because on one hand, not everyone starts their sentences
# with capital letters when chatting. On the other hand, the sentences are quite short, addressed directly to Odile.
# Is it necessary to limit the number of characters in a sentence?
# Again in this case it may be preferable to limit the number of words.
# The questions asked to Odile are supposed to be short, as too long sentences could interfere with the classification
# if they contain too much information.
# There is no universal answer. Everything will depend on the expected result.
#
# Exercise : Clean the dataset.
#
# Remove all unnecessary characters. You can choose to keep the smiley's or not.
"""

"""This method is very extreme by removing all ponctuations
So let's start with steps: 1 tokenization"""
# for column in data.columns:
#     data[column] = data[column].str.replace(r'\W', "")

""" this code is fine to tokenize a entire csv """
# import spacy
# import csv
# nlp = spacy.load("en_core_web_sm")
# doc = []
# with open(sentence) as csv_file:
#     csv_reader= csv.reader(csv_file)
#     for line in csv_reader:
#         for field in line:
#             # print(field)
#             doc.append(nlp(field))
# for item in doc:
#     for token in item:
#         print (token.text)
""" """
import spacy
from spacy.lang.en import English

import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

sent_tokenize(sentence)
# profile = ProfileReport(data, title="Pandas Profiling Report",  explorative=True)
# profile.to_file(output_file="Odile_wh_spec_charac.html")
# Put all sentences in lower case.
# Limit text to 256 words.