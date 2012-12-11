"""
   Shows how you can find the max value of a numpy array, then set the
   max value to zero for a 2-D array
"""
import numpy
myarray = numpy.array([[  5.4,   7.5,   2.2,   8.5,   8.6,   7.5],
                       [  7.7,   3.5,   1.4,   9.6,   8.5,   5.5],
                       [  5.2,   6.1,   8.6,   6.7,   4.3 ,  6.8],
                       [  9.6,   4.5,   2.7,   3.6,   6.7,   4.5],
                       [  1.2,   2.3,   7.2,   6.3,   2.2,   2.0 ],
                       [  1.3,   2.0,  -99.0,    9.6,  -99.0,    1.2]
                       ]
                      )
print myarray
maxValue = myarray.max()

itemindex = numpy.where(myarray >= maxValue)

for i in xrange(0, len(itemindex[0])):
    array1 = itemindex[0]
    array2 = itemindex[1]
    myarray[array1[i]][array2[i]] = 0

print myarray
