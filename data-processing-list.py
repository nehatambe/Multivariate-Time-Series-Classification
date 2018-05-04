import os
import csv
import pandas 
from random import shuffle
import time

start_time = time.time()

inputPath = "C:/FinalProject/Test/data/AReM"
colnames =['avg_rss12','var_rss12','avg_rss13','var_rss13','avg_rss23','var_rss23']


train_file_path = "C:/FinalProject/Test/data/Train.csv"
test_file_path = "C:/FinalProject/Test/data/Test.csv"

targetLength = 5
numOfInstances = 0
write_train_file = open(train_file_path,"w",newline='')
train_writer = csv.writer(write_train_file,dialect='excel',lineterminator='\n')

write_test_file = open(test_file_path,"w",newline='')
test_writer = csv.writer(write_test_file,dialect='excel')


rowList = []
row = []
classesDict = {}
class_counter = 1

#Method has logic to remove nan values. strip spaces
def processRowData(row):
   
    row = [val for val in row if str(val) != 'nan']
    row = [val for val in row if str(val) not in('var_rss12','var_rss13','var_rss23')]
   # row = [val.strip() for val in row]
    return row;


#def process_Train_Test_Data(row,train_writer,test_writer,fileName):
#    global numOfInstances
#    if row:
#        if fileName in fileNames:
#            numOfInstances = numOfInstances + 1
#            train_writer.writerow(row)
#        else:
#            test_writer.writerow(row)
            
            
def generate_interleaved_time_series(targetLength,row12,row13,row23,avgrow12):
    targetRow = []

    
    if targetLength == 0:
        targetRow.extend(row12)
        targetRow.extend(avgrow12)
        targetRow.extend(row13)
        #targetRow.extend(avgrow13)
        targetRow.extend(row23)
        #targetRow.extend(avgrow23)
        return targetRow
    
    row_len = len(row12)  
    start = 0
    end = targetLength
        
    while(row_len>= end):
        targetRow.extend(row12[start:end])
        targetRow.extend(avgrow12[start:end])
        targetRow.extend(row13[start:end])
        #targetRow.extend(avgrow13[start:end])
        targetRow.extend(row23[start:end])
        #targetRow.extend(avgrow23[start:end])
        start = end
        end = end + targetLength
        

    if(row_len - start!=0):
        end = row_len
        targetRow.extend(row12[start:end])
        targetRow.extend(avgrow12[start:end])
        targetRow.extend(row13[start:end])
        #targetRow.extend(avgrow13[start:end])
        targetRow.extend(row23[start:end])
        #targetRow.extend(avgrow23[start:end])
            
    return targetRow


def write_To_CSV(writeList, writer_name):
    for row in writeList:
        writer_name.writerow(row)
        

for root, subdirs, files in os.walk(inputPath):

    for filename in files:
        subdirname = os.path.basename(os.path.normpath(root))
        file_path = os.path.join(root, filename)
        
        data = pandas.read_csv(file_path, names=colnames)
        data = pandas.read_csv(file_path, names=colnames,comment='#', skiprows=5)
        row12 = data.var_rss12.tolist()
        row13 = data.var_rss13.tolist()
        row23 = data.var_rss23.tolist()
        avg12 = data.avg_rss12.tolist()
        avg13 = data.avg_rss13.tolist()
        avg23 = data.avg_rss23.tolist()
        
            
        row12 = processRowData(row12)
        row13 = processRowData(row13)
        row23 = processRowData(row23)
        avgrow12 = processRowData(avg12)
        avgrow13 = processRowData(avg13)
        avgrow23 = processRowData(avg23)
        
    
        
        if(subdirname not in classesDict):
            classesDict[subdirname] = class_counter
            class_counter += 1    
        
       
        row = generate_interleaved_time_series(targetLength,row12,row13,row23,avgrow12)
        
#        row = [int(0) if len(val)<1 else val for val in row] 
        
                
        if(len(row)>1):
            row.insert(0,classesDict[subdirname])
        
        if row:
            rowList.append(row)
        
#        if row:
#            if filename in fileNames:
#                train_writer.writerow(row)
#                numOfInstances = numOfInstances + 1
#            else:
#                test_writer.writerow(row)
        
  
shuffle(rowList)


trainList = rowList[:len(rowList)-10]
testList = rowList[len(rowList)-10:]

#write data to csv files
write_To_CSV(trainList, train_writer);
write_To_CSV(testList, test_writer);
            

print(time.time() - start_time)



