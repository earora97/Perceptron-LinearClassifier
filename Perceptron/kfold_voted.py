import csv
import numpy
from random import randrange
import nltk # needed for Naive-Bayes
import numpy as np
from sklearn.model_selection import KFold

def read_file(filename):
	raw_data = open(filename, 'rt')
	reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	x = list(reader)
	dataset = numpy.array(x)
	return dataset

def cross_validation_split(dataset, n_folds):
	data_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	data_split = list()
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(data_copy))
			fold.append(data_copy.pop(index))
		data_split.append(fold)
	return data_split


def algorithm(train_set,test_set):
	w=[]
	b=[]
	c=[]
	current_wvalue = []
	current_bvalue = 0
	current_cvalue = 1
	n= 1
	x = train_set[:,0:9]
	y = train_set[:,9]
	#print y
	num_inp2 = len(train_set)
	
	for i in range(dataset.shape[1]-1):
		current_wvalue.append(0)

	for curr_ite in range(n_epoch):
		for i in range(num_inp2):
			tsum=0
			var = 0
			if(int(y[i])==2):
		       		curr_y = -1
			else:
	        		curr_y = 1
	        	for k in range(dataset.shape[1]-1):
				var = var + current_wvalue[k]*int(x[i][k])
		   	tsum = tsum + var + current_bvalue
			if(curr_y*tsum <= 0):
				c.append(current_cvalue)
				b.append(current_bvalue)
				w.append(current_wvalue)
				n = n+1
				for k in range(dataset.shape[1]-1):	
					current_wvalue[k] = current_wvalue[k] + int(x[i][k])*curr_y
	       			current_bvalue = current_bvalue + curr_y
		 		current_cvalue = 1
			else:
				current_cvalue = current_cvalue + 1

	xx = test_set[:,0:9]
	yy = test_set[:,9]
	correct_predict = 0
	num_inp1 = len(test_set)

	for i in range(num_inp1):
		expected_yvalue = 0
		for j in range(len(w)):
			d=0
			for k in xrange(dataset.shape[1]-1):
                    		d = d + w[j][k]*int(xx[i][k])
               		expected_yvalue = expected_yvalue + c[j]*np.sign(d + b[j])
		if(expected_yvalue<0 and int(yy[i])==2):
			correct_predict = correct_predict + 1
		if(expected_yvalue>0 and int(yy[i])==4):
			correct_predict = correct_predict + 1

	return correct_predict


#### Initialisation ####
print ("Give filename:")
filename = raw_input()
dataset = read_file(filename)

n_epoch = 50
print ("Number of Epochs:", n_epoch)
input_rows = dataset.shape[0]
print ("Total number of rows are: ",input_rows)

kf = KFold(n_splits=10)
scores=[]
num_splits=10
#######    ########
#folds = cross_validation_split(dataset,num_splits)
#print folds

for train, test in kf.split(dataset):
    train_data = np.array(dataset)[train]
    test_data = np.array(dataset)[test]
    predicted = algorithm(train_data,test_data)
    scores.append(predicted)

num_row_per_case = float(input_rows)/float(num_splits)
print scores
print (float(np.mean(scores))/float(num_row_per_case))*100
