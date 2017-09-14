import pandas as pd
#import numpi as np


import pdb;pdb.set_trace()
df = pd.read_csv('train.csv',header=0)

print type(df)

print df.dtypes

print df.info()

print df.describe()

print df['Age'][0:10]


print df['Age'].mean()

print df[df['Age'] > 60]

print df[df['Age'] > 60][['Sex','Pclass','Age','Survived']]

print df[df['Age'] > 60][['Sex','Pclass','Age','Survived']].head(10)

print df[df['Age'].isnull()][['Sex','Pclass','Age']]

for i in range(1,4):
    print i , len([df[ df['Sex'] == 'male'] & (df['Pclass'] == i) ])


# Showing graph
import pylab as p
df['Age'].hist()
p.show()