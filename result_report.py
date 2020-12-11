#!/usr/bin/env python
# coding: utf-8

# In[513]:


# “An Analysis of Social Media Company’s User Agreement”  - Determining the readability 
# Katsuhiko Nakanishi


# import file
def file_import(file):
    f = open(file, encoding='utf-16')
    lines = f.readlines()
    f.close()
    
    punctuation = "!#$%&'\"()*+, -./:;<=>?@[\]^_`{|}~▪"
    
    # convert into a list of string
    flat_list = []
    for line in lines:
        # clean up data
        if line == '\n':
            continue
        line = line[:-1]
        line = line.lower()
        # replace panctuation
        for punc in punctuation: 
            line = line.replace(punc, " ")
            
        word = line.split()
            
        flat_list.extend(word)

    return flat_list

# test
file_import("facebook.txt")


# In[514]:


# import word list 
# 10k .txt = 10k most common English word (avg 8 years old)
# 20k .txt = 20k most common English word 
# 30k .txt = 30k most common English word 

# according to The Economist, average adult knows 20 - 35k words 35,000
# shakespeare used 25k unique words in his litreture  

def wordlist_import(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    
    # convert into a list of string
    data = []
    for line in lines:
        # clean up data
        line = line[:-1]
        if line[-1] == "\t":
            line = line[:-1]
        
        data.append(line)
        
    return data

# test
# wordlist_import("30k.txt")


# In[515]:


# total number words in the file
def total_num_words(file):
    file = file_import(file)
    count = len(file)
    
    return count

# bar chart of 5 file's size 
def size_bar(file1, file2, file3, file4, file5):
    
    file_list = [file1, file2, file3, file4, file5]
      
    for single_file in file_list:
        # total number words in the file
        size_result = total_num_words(single_file)
        # file name
        file_name = single_file.split(".")
        plt.bar(file_name[0], size_result, align='center', alpha=0.4)
        
        plt.xlabel('Name of the Company')
        plt.ylabel('Number of Words')
        plt.title("How Many Words are in the User's Agreement")
        
    plt.show()

# test
size_bar("reddit.txt", "facebook.txt", "instagram.txt", "twitter.txt", "linkedin.txt")


# In[516]:


def size_bar_var2(file1, file2, file3, file4, file5):
    
    file_list = [file1, file2, file3, file4, file5]
      
    for single_file in file_list:
        # total number words in the file
        size_result = total_num_words(single_file)
        # file name
        file_name = single_file.split(".")
        plt.bar(file_name[0], size_result, align='center', alpha=0.4)
        
        plt.xlabel('Name of the Company')
        plt.ylabel('Number of Words')
        plt.title("How Many Words are in the User's Agreement (in Data & Cookie section)")
        plt.xticks(rotation=90)
    plt.show()

# test
size_bar_var2("data_reddit.txt", "data_facebook.txt", "data_instagram.txt", "data_twitter.txt", "data_linkedin.txt")


# In[517]:


from collections import Counter
from wordcloud import WordCloud, STOPWORDS 

# frequency of of common words excluding stopwords
def freq_count(file):
    stopwords = STOPWORDS
    
    file = file_import(file)
    for word in file:
        # remove stopwords
        for i in stopwords:
            if word == i:
                file.remove(word)
    # count frequency
    counted = Counter(file)
    # oder by the most common / frequenct 
    counted_ordered = counted.most_common()
    
    return counted_ordered

# test
freq_count("reddit.txt")


# In[518]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

# return the wordcloud
def word_cloud(file):
    # convert into a string
    file = file_import(file)
    # file name
    unique_string = (" ").join(file)

    # generate the wordcloud object, 
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', collocations=False, stopwords = STOPWORDS).generate(unique_string)
    
    # draw the figure
    plt.figure(figsize=(40, 30))
    # display image
    plt.imshow(wordcloud) 
    # no axis 
    plt.axis("off")
    plt.show()
    plt.close()

#  test
word_cloud('reddit.txt')
# word_cloud('facebook.txt')
# word_cloud('instagram.txt')
# word_cloud('twitter.txt')
# word_cloud('linkedin.txt')


# In[519]:


def compare_common(file, wordlist):
    # total number words in the file
    size = total_num_words(file)
    # import and convert file 
    file = file_import(file)
    # import and convert wordlist
    wordlist = wordlist_import(wordlist)
    
    # base case for counter
    counter = 0
    for i in file:
        if i in wordlist:
            counter += 1
    
    # normalization
    result = (counter / size) * 100

    return result

# test
compare_common("facebook.txt", "10k.txt")


# In[520]:


import matplotlib.pyplot as plt

def scatter(file1, file2, file3, file4, file5, wordlist):
    
    file_list = [file1, file2, file3, file4, file5]
    # word list file name
    wordlist_name = wordlist.split(".")
    
    # plot size
    plt.figure(figsize=(10,10))
    
    for single_file in file_list:
        # file name
        file_name = single_file.split(".")
        # return the score of frequency 
        freq_result = compare_common(single_file, wordlist)
        # returns the size of the file
        size_result = total_num_words(single_file)
        
        # scatter plot
        plt.scatter(freq_result, size_result, label=file_name[0], s=70)
        
    plt.grid()

    plt.xlabel('Frequency of Words found in the ' + wordlist_name[0] + ' Word List (%)', fontsize=12)
    plt.ylabel('Document Size (number of words)', fontsize=12)
    plt.title('Readability of Documents ' + wordlist_name[0], fontsize=20)

    # create legend
    plt.legend()

# test
scatter("reddit.txt", "facebook.txt", "instagram.txt", "twitter.txt", "linkedin.txt", "10k.txt")


# In[521]:


import matplotlib.pyplot as plt

def data_scatter(file1, file2, file3, file4, file5, wordlist):
    
    file_list = [file1, file2, file3, file4, file5]
    # word list file name
    wordlist_name = wordlist.split(".")
    
    # plot size
    plt.figure(figsize=(10,10))
    
    for single_file in file_list:
        # file name
        file_name = single_file.split(".")
        # return the score of frequency 
        freq_result = compare_common(single_file, wordlist)
        # returns the size of the file
        size_result = total_num_words(single_file)
        
        # scatter plot
        plt.scatter(freq_result, size_result, label=file_name[0], s=70)
        
    plt.grid()
    plt.xlabel('Frequency of Words found in the ' + wordlist_name[0] + ' Word List (%)', fontsize=12)
    plt.ylabel('Document Size (number of words)', fontsize=12)
    plt.title('Readability of Data & Cookie Documents ' + wordlist_name[0], fontsize=20)

    # create legend
    plt.legend()

# test
data_scatter("data_reddit.txt", "data_facebook.txt", "data_instagram.txt", "data_twitter.txt", "data_linkedin.txt", "10k.txt")


# In[522]:


import matplotlib.pyplot as plt

# count words from file that are included inside CCPA
def ccpa_compare_common(file, ccpa):
    # total number words in the file
    size = total_num_words(file)
    # import and convert file 
    file = file_import(file)
    # import and convert ccpa
    ccpa = file_import(ccpa)
    
    # base case for counter
    counter = 0
    for i in file:
        if i in ccpa:
            counter += 1
    
    # normalization
    result = (counter / size) * 100

    return result

# ccpa version of similality test
def ccpa_scatter(file1, file2, file3, file4, file5, ccpa):
    
    file_list = [file1, file2, file3, file4, file5]
    
    # plot size
    plt.figure(figsize=(10,10))
    
    for single_file in file_list:
        # file name
        file_name = single_file.split(".")
        # return the score of frequency 
        freq_result = ccpa_compare_common(single_file, ccpa)
        # returns the size of the file
        size_result = total_num_words(single_file)
        
         # scatter plot
        plt.scatter(freq_result, size_result, label=file_name[0], s=70)
    
    plt.grid()
    plt.xlabel('Frequency of Words Found in CCPA (%)', fontsize=12)
    plt.ylabel('Document Size (number of words)', fontsize=12)
    plt.title('How Similar is the Document to CCPA', fontsize=20)

    # create legend
    plt.legend()


ccpa_scatter("reddit.txt", "facebook.txt", "instagram.txt", "twitter.txt", "linkedin.txt", "CCPA2018.txt")


# In[523]:


# ccpa data version of similality test
def data_ccpa_scatter(file1, file2, file3, file4, file5, ccpa):
    
    file_list = [file1, file2, file3, file4, file5]
    
    # plot size
    plt.figure(figsize=(10,10))
    
    for single_file in file_list:
        # file name
        file_name = single_file.split(".")
        # frequency count
        freq_result = ccpa_compare_common(single_file, ccpa)
        # size of the file
        size_result = total_num_words(single_file)
        
        # scatter plot
        plt.scatter(freq_result, size_result, label=file_name[0], s=70)
    
    plt.grid()
    plt.xlabel('Frequency of Words Found in CCPA (%)', fontsize=12)
    plt.ylabel('Document Size (number of words)', fontsize=12)
    plt.title('How Similar are Data & Cookie Documents to CCPA', fontsize=20)

    # create legend
    plt.legend()

# test
data_ccpa_scatter("data_reddit.txt", "data_facebook.txt", "data_instagram.txt", "data_twitter.txt", "data_linkedin.txt", "CCPA2018.txt")


# In[524]:


from IPython.display import display, Math
# The Flesch–Kincaid readability tests are readability tests and indicate how difficult a passage in English is to understand.
# higher scores indicate material that is easier to read; lower numbers mark passages that are more difficult to read.
# see table in my slide to see the socre table

# formula 
display(Math(r'{\displaystyle 206.835-1.015\left({\frac {\text{total words}}{\text{total sentences}}}\right)-84.6\left({\frac {\text{total syllables}}{\text{total words}}}\right)}'))


# In[525]:


from IPython.display import display, Math

# The Flesch-Kincaid Grade Level
# formula 
display(Math(r'{\displaystyle 0.39\left({\frac {\mbox{total words}}{\mbox{total sentences}}}\right)+11.8\left({\frac {\mbox{total syllables}}{\mbox{total words}}}\right)-15.59}'))


# In[526]:


from IPython.display import display, Math

# The Fog Scale (Gunning FOG Formula)
# formula 
display(Math(r'0.4\left[\left({\frac  {{\mbox{words}}}{{\mbox{sentences}}}}\right)+100\left({\frac  {{\mbox{complex words}}}{{\mbox{words}}}}\right)\right]'))


# In[527]:


# instead of list of string, new test reuqires a sentences
def file_import_var2(file):
    f = open(file, encoding='utf-16')
    lines = f.readlines()
    f.close()
    
    flat_list = []
    for line in lines:
        if line[:-1] == '\n':
            continue
        line = line[:-1]
             
        flat_list.append(line)

    return flat_list

# test
file_import_var2("reddit.txt")


# In[529]:


import pandas as pd
from astropy.table import QTable, Table, Column
from astropy import units as u
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table 

def flesch_var2(file):
    # file name
    file_name = file.split(".")
    # convert into a sentences
    file = file_import_var2(file)    
    file_str = (" ").join(file)
      
    # The Flesch Reading Ease formula
    # 90-100: Very Easy, 0-29: Very Confusing
    result_reading_ease = textstat.flesch_reading_ease(file_str)
    
    # The Flesch-Kincaid Grade Level
    # 9.3 means that a ninth grader would be able to read the document
    result_kincaid_grade = textstat.flesch_kincaid_grade(file_str)
    
    # The Fog Scale (Gunning FOG Formula)
    # 9.3 means that a ninth grader would be able to read the document
    result_fog = textstat.gunning_fog(file_str)
    
    # dictionary of the result
    data = {'score of ' + file_name[0]:  [result_reading_ease, result_kincaid_grade, result_fog],
            'formula': ["The Flesch Reading Ease", "The Flesch-Kincaid Grade Level", "The Fog Scale"]}
    
    # data frame
    df = pd.DataFrame (data, columns = ['formula', 'score of ' + file_name[0]])
    blankIndex=[''] * len(df)
    df.index=blankIndex # hide the index
    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    table(ax, df, rowLabels=['']*df.shape[0], loc='center')
    
    # uncomment below to save the image
    #plt.savefig('mytable.png')
    
    return df

# test
flesch_var2("data_instagram.txt")
#flesch_var2("facebook.txt")
#flesch_var2("instagram.txt")
#flesch_var2("twitter.txt")
#flesch_var2("linkedin.txt")

#flesch_var2("data_reddit.txt")
#flesch_var2("data_facebook.txt")
#flesch_var2("data_instagram.txt")
#flesch_var2("data_twitter.txt")
#flesch_var2("data_linkedin.txt")


# In[ ]:




