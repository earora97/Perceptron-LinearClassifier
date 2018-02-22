import csv
import numpy
import nltk
import sklearn

def read_file(filename):
	raw_data = open(filename, 'rt')
	reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	x = list(reader)
	data = numpy.array(x)
	print data
	return data

def voted_perceptron():
	
	w=[]
	b=[]
	c=[]
	n=1
	current_wvalue = []
	current_bvalue = []
	current_cvalue = 1
	
	#Initialising w and b
	for i in range(dataset.shape[1]-1):
		current_wvalue.append(0)
	for i in range(dataset.shape[1]-1):
		current_bvalue.append(0)
	
	for curr_ite in range(n_epoch):
		for i in xrange(input_rows):
			tsum=0
		        for k in xrange(dataset.shape[1]-1):
					tsum=tsum+current_wvalue[k]*int(x[i][k])+current_bvalue[k]
			if(int(y[i])==2):
		       		curr_y = -1
			else:
	        		curr_y = 1
		   	if(curr_y*tsum <=0):
				n = n+1
				c.append(current_cvalue)
				b.append(current_bvalue)
				w.append(current_wvalue)
				for k in xrange(dataset.shape[1]-1):	
			            current_wvalue[k] = current_wvalue[k] + int(x[i][k])*curr_y
	       			    current_bvalue[k] = current_bvalue[k] + curr_y
		 		    current_cvalue = 1
			else:
				current_cvalue = current_cvalue + 1
	return w,b,c,n

def prediction(w,b,c,n):
	right_predict = 0
	for i in xrange(input_rows):
		expected_yvalue = 0
		for j in xrange(n-1):
			for k in xrange(dataset.shape[1]-1):
				expected_yvalue = expected_yvalue + w[j][k]*int(x[i][k]) + b[j][k]
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