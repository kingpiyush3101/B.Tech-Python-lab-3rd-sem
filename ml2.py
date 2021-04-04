#Python Programming for Loading the Data
'''import numpy as np
import pandas as pd
import pickle
def load_csv(filepath):
    data=[]
    col=[]
    cheakcol=False #Boolean variable
    with open(filepath) as f:
        for val in f.readlines():
            val=val.replace("\n","")
            val=val.split(',')
            if cheakcol is False:
                col=val
                cheakcol=True
            else:
                data.append(val)
                df=pd/DataFrame(data=data,columns=col)
                return df
myData=load_csv('abc.data.csv')
print(myData.head())
'''

#Python Programming for Multinomial Distribution
'''from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)'''

#Visualization of Binomial Distribution
'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()'''

#mean/mode/median
'''import numpy
from scipy import stats #for mode import ststs i.e, statics from scipy
speed=[99,86,87,88,111,86,103,87,94,78,77,85,86]
x=numpy.mean(speed)
print("Average speed :",x)
y=numpy.median(speed)
print("Mid point value :",y) #list is sorted before finding median
#in case of odd no. of elements the two no. at middle are added and then divided by 2 to get mid point value
z=stats.mode(speed)
print("Value that appears most time:",z)'''