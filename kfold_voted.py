import csv
import numpy
from random import randrange

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

def read_file(filename):
	raw_data = open(filename, 'rt')
	reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	x = list(reader)
	try:
		data = numpy.array(x).astype('float')
	except ValueError:
		data = numpy.array(x)
	return data
#print(data.shape)

def algorithm(train_set,test_set):
	w=[]
	b=[]
	c=[]
	curr_w = []
	curr_b = []
	curr_c = 1
	n= 1

	for i in range(data.shape[1]-1):
		curr_w.append(0)
	for i in range(data.shape[1]-1):
		curr_b.append(0)

	for curr_ite in range(n_epoch):
		for i in xrange(num_inp):
			tsum=0
			#print "i",i
		        for k in xrange(data.shape[1]-1):
					tsum=tsum+curr_w[k]*int(x[i][k])+curr_b[k]
			#print tsum
			if(int(y[i])==2):
		       		curr_y = -1
			else:
	        		curr_y = 1
			#print curr_y	    	
		   	if(curr_y*tsum <=0):
					
				w.append(curr_w)
				b.append(curr_b)
				c.append(curr_c)
				n = n+1
				for k in xrange(data.shape[1]-1):	
			            curr_w[k] = curr_w[k] + int(x[i][k])*curr_y
	       			    curr_b[k] = curr_b[k] + curr_y
		 		    curr_c = 1
			else:
				curr_c = curr_c + 1
	correct = 0
	for i in xrange(num_inp):
		epx_y = 0
		for j in xrange(n-1):
			for k in xrange(data.shape[1]-1):
				epx_y = epx_y + w[j][k]*int(x[i][k]) + b[j][k]
		if(epx_y<0 and int(y[i])==2):
			correct = correct + 1
		if(epx_y>0 and int(y[i])==4):
			correct = correct + 1

	return correct

#print "W",w
#print "B",b
#print "C",c

#def prediction():
	

filename = './breast_edit.csv'
n_epoch = 50

data = read_file(filename)
data  = data[0:6,:]
#print data
x = data[:,0:9]
#print x #print type(x[0][1]) #print(x[0]);
y = data[:,9]
#print(y) #print type(y[0])
num_inp = data.shape[0]

n_folds = 2

folds = cross_validation_split(data, n_folds)
scores = list()
for fold in folds:
	train_set = list(folds)
	train_set.remove(fold)
	train_set = sum(train_set, [])
	test_set = list()
	for row in fold:
		row_copy = list(row)
		test_set.append(row_copy)

	predicted = algorithm(train_set,test_set)
	scores.append(predicted)
print scores