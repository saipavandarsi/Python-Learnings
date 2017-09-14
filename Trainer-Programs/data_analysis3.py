import pandas as pd
#import numpy as np

# For .read_csv, always use header=0 when you know row 0 is the header row
import pdb;pdb.set_trace()
df = pd.read_csv('train.csv', header=0)

print type(df)

print df.dtypes

print df.info()

print df.describe()

print df['Age'][0:10]

print df['Age'].mean()

print df[ ['Sex', 'Pclass', 'Age'] ]

print df[df['Age'] > 60]

print df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]

print df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']].head(10)

print df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i) ])
	
# showing graph

import pylab as P
df['Age'].hist()
P.show()