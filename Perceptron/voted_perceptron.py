import csv
import numpy as np
import nltk
import sklearn

def read_file(filename):
	raw_data = open(filename, 'rt')
	reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	x = list(reader)
	data = np.array(x)
	#print data
	return data

def voted_perceptron():
	b=[]
	w=[]
	c=[]
	n=1
	newsum=[]
	current_wvalue = []
	current_bvalue = 0
	current_cvalue = 1
	
	#Initialising w
	for i in range(dataset.shape[1]-1):
		current_wvalue.append(0)
	
	#print input_rows
	for curr_ite in range(n_epoch):
		for i in xrange(input_rows):
			tsum=0
			if(int(y[i])==2):
		       		curr_y = -1
			else:
	        		curr_y = 1
	        	tsum=0
			var=0
			for k in range(dataset.shape[1]-1):
				var = var + current_wvalue[k]*int(x[i][k])
		   	tsum = tsum + var + current_bvalue		        	
				
			if(curr_y*tsum <= 0):
				c.append(current_cvalue)
				b.append(current_bvalue)
				w.append(current_wvalue)
				n = n+1
				for k in xrange(dataset.shape[1]-1):	
					current_wvalue[k] = current_wvalue[k] + int(x[i][k])*curr_y
	       			current_bvalue = current_bvalue + curr_y
		 		current_cvalue = 1
			else:
				current_cvalue = current_cvalue + 1
	#print w
	return w,b,c,n

def prediction(w,b,c,n):
	right_predict = 0
	for i in xrange(input_rows):
		expected_yvalue = 0
		for j in xrange(n-1):
			d=0
			for k in xrange(dataset.shape[1]-1):
				d = d + w[j][k]*int(x[i][k])
			expected_yvalue = expected_yvalue + c[j]*np.sign(d + b[j])
		if(expected_yvalue>0 and int(y[i])==4):
			right_predict = right_predict + 1
		if(expected_yvalue<0 and int(y[i])==2):
			right_predict = right_predict + 1
		

	print ("Total correct predictions:", right_predict)
	return right_predict

print ("Give filename:")
filename = raw_input()
dataset = read_file(filename)


#### Initialisation ####
n_epoch = 50
print ("Number of Epochs:", n_epoch)
input_rows = dataset.shape[0]
print ("Total number of rows are: ",input_rows)
x = dataset[:,0:9]
y = dataset[:,9]
#######    ########


final_w, final_b, final_c , final_n = voted_perceptron()
correct_predictions = prediction(final_w,final_b,final_c,final_n)
print 100*(float(correct_predictions)/float(input_rows))
