from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Series

obj = Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print(obj2['b'])

# Filtering & Simple Operations
print(obj2[obj2 > 0])
print(obj2 * 2)

print('c' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = Series(sdata, index=states)
print(obj4)

print(pd.isnull(obj4))

print(obj3 + obj4)

# DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)

print(DataFrame(data, columns=['year', 'state', 'pop']))

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2.columns)

print(frame2['state'])
print(frame2.year)
print(frame2.year[frame2.year > 2000])

print(frame2.ix['three'])

frame2['debt'] = 16.5
print(frame2)

frame2['debt'] = np.arange(5.)

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

# add new column
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

# remove column
del frame2['eastern']
print(frame2)



pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
print(frame3)

# Easily transposing!
print(frame3.T)

print(frame2)
print(frame2.drop(['one','two','three']))