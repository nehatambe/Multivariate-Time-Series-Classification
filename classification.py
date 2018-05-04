# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:02:05 2018

@author: nehatambe
"""
import csv
from ctypes import windll, c_long, c_char_p


extractedFilePath = "C:/FinalProject/Test/data/Train_tree"
test_file_path = "C:/FinalProject/Test/data/Test.csv"


csvReader = csv.reader(open(test_file_path, "r+"))
numOfInstances = len(list(csvReader))
print(numOfInstances)

test =  windll.LoadLibrary("C:/FinalProject/Test/classification/x64/Debug/classify.dll")
numOfInstances = c_long(numOfInstances)
numOfClasses = c_long(6)

filePath = c_char_p(test_file_path.encode('utf-8'))
extractedFilePath = c_char_p(extractedFilePath.encode('utf-8'))

count = test.classifySeriesData(numOfInstances,numOfClasses,filePath,extractedFilePath)
print(count)

