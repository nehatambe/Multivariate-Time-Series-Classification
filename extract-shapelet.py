# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 00:39:19 2018

@author: nehatambe
"""
import csv
from ctypes import windll, c_long, c_char_p


startLength = c_long(1400)
endLength = c_long(200) 
stepSize = c_long(100)
numOfClasses = c_long(7)

train_file_path = "C:/FinalProject/Test/data/Train.csv"
tree_file_path = "C:/FinalProject/Test/data/Train"
filePath = c_char_p(train_file_path.encode('utf-8'))
writeFilePath = c_char_p(tree_file_path.encode('utf-8'))

csvReader = csv.reader(open(train_file_path, "r+"))
numOfInstances = len(list(csvReader))


test =  windll.LoadLibrary("C:/FinalProject/Test/shapelet/x64/Debug/ShapeletTest.dll")

numOfInstances = c_long(numOfInstances)

test.extractShapelet(numOfInstances,numOfClasses, filePath, writeFilePath,startLength, endLength, stepSize)


