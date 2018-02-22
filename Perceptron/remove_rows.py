import csv
import numpy
import nltk
import sklearn

final_output = open('output.csv', 'wb')
initial_input = open('breast.csv', 'rb')
filename = './breast.csv'
writer = csv.writer(final_output)

raw = open(filename, 'rt')
reader = csv.reader(raw, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)

value = numpy.array(x)
print value

rangex = value.shape[1]-1
print ("Number of columns are",rangex)
count=0

# Traverse over all the values in row and if we find any question mark, mark flag as not equal to 0 and break the loop

for current_row in csv.reader(initial_input):
    flag=0
    for j in xrange(rangex):
        if current_row[j]=='?':
            flag=1
            count = count + 1
    if flag==0:
#        print current_row
        writer.writerow(current_row)

print ("Number of rows with ? are : " , count)

print ("New file with filename output.csv Saved!")
#close both the files

initial_input.close()
final_output.close()