#Create Comma Separate Files (CSV)
'''import csv
with open('student.csv', 'w') as csvfile:
    wrt=csv.writer(csvfile)
    for i in range(5):
        n=input("Enter Name: ")
        a=input("Enter Address: ")
        b=input("Enter Branch: ")  
        wrt.writerow([n,a,b])'''

#Load CSV files into internal Data Structure
'''import csv
import numpy
filename='abc.data.csv'
raw_data=open(filename,'rt')
reader=csv.reader(raw_data,delimiter=',',quoting=csv.QUOTE_NONE)
x=list(reader)
data=numpy.array(x).astype('float')
print(data.shape)'''

#data distribution

#create array containing 250 random float between 0 and 5
'''import numpy
x=numpy.random.uniform(0.0,5.0,250)
print(x)
#create histogram of above data
import matplotlib.pyplot as plt
plt.hist(x,5)
plt.show()'''
#array with 100000 random numbers with 100 bars
'''import numpy
import matplotlib.pyplot as plt
x=numpy.random.uniform(0,500,100000)
print(x)
plt.hist(x,100)
plt.show()'''
#scatter plot
'''import matplotlib.pyplot as plt
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86] #x and y length should be same
plt.scatter(x,y)
plt.show()'''
#linear regrassion
'''import matplotlib.pyplot as plt
from scipy import stats
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def myfunc(x):
    return slope*x + intercept
mymodel=list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()'''
