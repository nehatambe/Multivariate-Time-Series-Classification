# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:58:46 2018

@author: nehatambe
"""

import os
import time
import pandas 
from random import shuffle
from pandas import DataFrame

start_time = time.time()

inputPath = "C:/FinalProject/Test/data/AReM"
colnames =['var_rss12','var_rss13','var_rss23']


train_file_path = "C:/FinalProject/Test/data/Train.csv"
test_file_path = "C:/FinalProject/Test/data/Test.csv"


targetLength = 5


rowList = []
row = []
classesDict = {}
class_counter = 1
df = DataFrame()



def merge(data):
    start = 0
    end = targetLength
    while(end<=480):
            test = data[start:end]
            vertical_stack = pandas.concat([test['var_rss12'],test['var_rss13'],test['var_rss23']], axis=0)
            row.extend(vertical_stack)
            #df = df.append(vertical_stack,ignore_index=True)
            start = end
            end+= targetLength
            
    return row

for root, subdirs, files in os.walk(inputPath):

    for filename in files:
        subdirname = os.path.basename(os.path.normpath(root))
        file_path = os.path.join(root, filename)
        
        data = pandas.read_csv(file_path, names=colnames,comment='#', skiprows=5)
        row.clear()
        row = merge(data)
#        start = 0
#        end = targetLength
        
        if(subdirname not in classesDict):
            classesDict[subdirname] = class_counter
            class_counter += 1
            
        if(len(row)>1):
            row.insert(0,classesDict[subdirname])
            
        rowList.append(row[:])
        
           
shuffle(rowList)
trainList = rowList[:len(rowList)-10]
testList = rowList[len(rowList)-10:]

train_df = pandas.DataFrame(trainList)
train_df.to_csv(train_file_path, index = False, header = False)

test_df = pandas.DataFrame(testList)
test_df.to_csv(test_file_path, index = False, header = False)           

print(time.time() - start_time)
