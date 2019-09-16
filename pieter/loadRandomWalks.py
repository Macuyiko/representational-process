import gensim
import os
import re
import numpy as np
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim.models.doc2vec import TaggedDocument
import random

def get_doc_list(folder_name, walks_name):
    doc_list = []
    file_list = ['input/'+folder_name+'/'+walks_name+'/'+name for name in os.listdir('input/'+folder_name+'/'+walks_name) if name.endswith('txt')]
    print ('Found %s documents under the dir %s .....'%(len(file_list),folder_name))
    return file_list

def get_doc(folder_name, walks_name, ignore_gateways=False):
    doc_list = get_doc_list(folder_name,walks_name)
    taggeddocs = []
    for index, i in enumerate(doc_list):
        docpre = i.split('/')[-1].replace('.txt', '')
        file = open(i, 'r')
        for line in file.readlines():
            line = line.replace('Activity ', 'Activity_')
            cleanwalk = []
            for word in line.split(' '):
                if ignore_gateways and ('DATABASE' in word or 'PLACE' in word):
                    continue
                if '+' in word:
                    word = word.replace("+","")
                cleanwalk.append(word)
            td = TaggedDocument(gensim.utils.to_unicode(str.encode(' '.join(cleanwalk))).split(), [str(i)])
            taggeddocs.append(td)
    random.shuffle(taggeddocs)
    return taggeddocs

def get_doc_stats(folder_name,walks_name):
    doc_list = get_doc_list(folder_name,walks_name)
    tokenizer = RegexpTokenizer(r'\w+')
    length_array=[]
    for index,i in enumerate(doc_list):
        file = open(i,'r')
        wordslist = []
        tagslist = []
        for line in file.readlines():
            cleanwalk= []
            for word in line.split(' '):
                if ('%GWC%' in word):
                    splitword= word.split('%GWC%')
                    cleanwalk.append(splitword[0])
                elif '+' in word:
                    cleanwalk.append(word.replace("+",""))
                else:
                    cleanwalk.append(word)
            length_array.append(len(cleanwalk))
    length_np= np.array(length_array)
    print('Average: ',str(length_np.mean()), ' St_dev: ', str(np.std(length_np)))

