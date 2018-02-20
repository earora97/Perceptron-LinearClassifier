import csv
import numpy
input = open('breast.csv', 'rb')
output = open('breast_edit.csv', 'wb')
filename = '/home/sailaja/Documents/sem6/smai/breast.csv'
writer = csv.writer(output)
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
try:
  data = numpy.array(x).astype('float')
except ValueError:
   data = numpy.array(x)
print(data.shape)
for row in csv.reader(input):
    b=0
    for j in xrange(data.shape[1]-1):
    #print row
        if row[j]=='?':
            b=1
    if b==0:
        writer.writerow(row)
input.close()
output.close()
