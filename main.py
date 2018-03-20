import os
import csv
import pandas 
inputPath = "C:/FinalProject/research/Datasets/AReM"
colnames =['time','avg_rss12','var_rss12','avg_rss13','var_rss13','avg_rss23','var_rss23']
classes ={'bending1':0,'bending2':1,'cycling':2,'lying':3,'sitting':4,'standing':5,'walking':6}
trainfilepath = "C:/FinalProject/Test/shapelet/train.csv"
writefile = open(trainfilepath,"w+",newline='')
writer = csv.writer(writefile,dialect='excel')

for root, subdirs, files in os.walk(inputPath):

    for filename in files:
        subdirname = os.path.basename(os.path.normpath(root))
        file_path = os.path.join(root, filename)
        
        data = pandas.read_csv(file_path, names=colnames)
        rows = data.var_rss12.tolist()
        rows = [row for row in rows if str(row) != 'nan']
        rows = [row for row in rows if str(row) != 'var_rss12']
        classname = classes[subdirname]
        if(len(rows)>1):
            rows.insert(0,classname)
        writer.writerow(rows)
        #for val in rows:
         #   writer.writerow(val)
        
        #print(rows)
        #values = csv.reader(open(file_path))
        #for row in values:
         #   if (len(row) < 1) or (row[0].startswith('#')):
          #      continue
           # print(row[2])
        #print('\t- file %s (full path: %s)' % (filename, file_path))
    
    

#from ctypes import windll, c_long, c_int, c_char_p
#test =  windll.LoadLibrary("C:/FinalProject/Test/shapelet/x64/Debug/ShapeletTest.dll")
#numOfInstances = c_long(60)
#numOfClasses = c_long(4)
#maxLength = c_long(300)
#minLength = c_long(10) 
#path = 'C:/FinalProject/Test/shapelet/Car_TRAIN';
#filePath = c_char_p(path.encode('utf-8'))
#test.extractShapelet(numOfInstances,numOfClasses, filePath, maxLength, minLength)
