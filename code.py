from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
def extract_features(words):
    return dict([(word, True) for word in words])

#import nltk
#nltk.download('movie_reviews')

def SentimentAnalyzer(text):
    # load movie reviews from sample data
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in fileids_neg]

    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))

    # creating training and testing data
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]

    #print('\nNumber of training datapoints:', len(features_train))
    #print('Number of test datapoints:', len(features_test))

    # training a naive bayes classifier 
    classifier = NaiveBayesClassifier.train(features_train)
    print('Accuracy:',nltk_accuracy(classifier, features_test))

    probabilities = classifier.prob_classify(extract_features(text.split()))
    # Pick the maximum value
    predicted_sentiment = probabilities.max()
    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:",round(probabilities.prob(predicted_sentiment), 2))

    return predicted_sentiment  

def ChatAnalyzer(text):
    bot=ChatBot("aicc",logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.BestMatch'
    ],  
    prepocessors=[
    'chatterbot.preprocessors.clean_whitespace'
    ]
    )
    trainer=ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')
    conversation=[
    "Hello",
    "Hi There",
    "What is your name?",
    "My name is aiccbot",
    "Thank You",
    "Welcome"

    ]
    trainer=ListTrainer(bot)
    trainer.train(conversation)
    answer=bot.get_response(text)
    return answer

def predict_career(a):
     c=DecisionTreeClassifier()
     x1=[[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1],[0,0,1,1,1],[0,1,1,1,1]]
     y1=['yes','yes','yes','no','no','no','no','no','yes','yes']
     c=c.fit(x1,y1)
     p1=c.predict(a)
     return p1


def chart(a,b):
    plt.title="Your Test Report"
    plt.bar(a,b)
    plt.show()

