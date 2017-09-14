import pandas as pd

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}

cities = pd.Series(d)

print cities

print cities['Chicago']

print cities[['Chicago', 'Portland', 'San Francisco']]

print cities[cities < 1000]

print cities/3