import csv
import numpy

####Reading csv file####
filename = './breast.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
try:
	data = numpy.array(x).astype('float')
except ValueError:
	data = numpy.array(x)
#print(data.shape)
#######    ########


##### Storing x and y #####

x = data[:,0:9]
#print type(x[0][1])
#print(x[0]);
y = data[:,9]
#print(y)
#print type(y[0])

#######    ########

#### Initialising ####
n_epoch = 500
num_inp = data.shape[0]

w=[]
b=[]
c=[]
curr_w = []
curr_b = []
curr_c = 1
n=1
for i in range(data.shape[1]):
	curr_w.append(0)
for i in range(data.shape[1]):
	curr_b.append(0)

#######    ########

for curr_ite in range(n_epoch):
	for i in xrange(num_inp):
		tsum=0
        for k in xrange(data.shape[1]-1):
			tsum=tsum+curr_w[k]*int(x[i][k])+curr_b[k]
	        
			if(y[i]==2):
	        		curr_y = -1
			else:
	        		curr_y = 1
	    	
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

print "W",w
print "B",b
print "C",c