#!/usr/bin/env python
# coding: utf-8

# In[14]:


## This list will be used to remove all the punctuations from the tweet
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

##Opening the file that contains fake generated tweet
project_twitter_file = open('project_twitter_data.csv','r')

## Creating a csv file containing the data for positive and negative sentiments
project_create_file = open('resulting_data.csv','w')

## Function to remove all punctuations
def strip_punctuation(word):

    for achar in punctuation_chars:
        word = word.replace(achar, '')

    return word

## Function to count number of positive words

def get_pos(word_1):
    ## Calling the strip function to remove all thepunctuations in the tweets
    word_1 = strip_punctuation(word_1)
    
    ## Converting all the letters into lowercase
    word_1 = word_1.lower()
    
    ## Spliting the tweet into words so that they can be used to count the positive words
    word_1 = word_1.split()      
    count=0
    for word in word_1:
        if word in positive_words:
              count+=1
    return count

## Function to count negative words

def get_neg(word_2):
     ## Calling the strip function to remove all thepunctuations in the tweets
    word_2 = strip_punctuation(word_2)
    ## Converting all the letters into lowercase
    word_2 = word_2.lower()
     ## Spliting the tweet into words so that they can be used to count the negative words
    word_2 = word_2.split()      
    count=0
    for word in word_2:
        if word in negative_words:
              count+=1
    return count


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
#Creating a file to count number of retweets, number of replies, positive score, negative score and net score
def creating_datafile(project_create_file):
    project_create_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    project_create_file.write("\n")

    linesPTDF =  project_twitter_file.readlines()
    
    ## Removing the headers from the tweet
    headerDontUsed= linesPTDF.pop(0)
    ## Creating the file to store the tweet data
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        project_create_file.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        project_create_file.write("\n")

        
## Calling the function to open the project file for data storing
creating_datafile(project_create_file)
## Closing the fake tweet data files
project_twitter_file.close()
## Closing the file created to read the data
project_create_file.close()


# In[15]:


import seaborn as sns


# In[17]:


import pandas as pd
project_twitter_file


# In[ ]:




