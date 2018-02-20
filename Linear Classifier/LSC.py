import sys
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from pylab import *

def LeastSquareClassifier(inputData):
 A=[x[1:] for x in inputData]
 print A
 A=np.insert(A, 2 ,1 ,axis=1)
 print A
 m = np.matrix(A)
 t = m.getT()
 mul = t*m
 inv = mul.getI()
 secondMul = inv * t
 print secondMul

 b = np.matrix([x[0] for x in inputData])
 bt = b.getT()
 print b

 f = secondMul * bt
 print f

 weightPlot = []
 weightPlot.insert(0,f.item(0))
 weightPlot.insert(1,f.item(1))
 weightPlot.insert(2,f.item(2))
 return weightPlot

#start
if __name__ == '__main__':
 inputData = [[1,-1,-1], [1,-1,1], [1,0,0], [1,1,0], [-1,2,1], [-1,3,0], [-1,3,3], [-1,0,1]]
 weightPlotLS = LeastSquareClassifier(inputData)
 a = weightPlotLS[0]
 b = weightPlotLS[1]
 c = weightPlotLS[2]
 x=arange(0,10,1)
 y=[(-1*c-a*i)/b for i in x]
 plot(x,y)

 pt1x=[i[1] for i in inputData[:4]]
 pt1y=[i[2] for i in inputData[:4]]
 plot(pt1x, pt1y, 'ro')
 pt2x=[i[1] for i in inputData[4:]]
 pt2y=[i[2] for i in inputData[4:]]
 plot(pt2x, pt2y, 'bo')

 show()